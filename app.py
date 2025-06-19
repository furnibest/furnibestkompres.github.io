from flask import Flask, render_template, request, send_file, send_from_directory # type: ignore
from PIL import Image
import io
import os
import logging
from werkzeug.utils import secure_filename # type: ignore

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Create uploads directory if it doesn't exist
if not os.path.exists('uploads'):
    os.makedirs('uploads')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

@app.route('/compress', methods=['POST'])
def compress_image():
    try:
        # Check if file exists in request
        if 'image' not in request.files:
            logger.error("No image file in request")
            return 'No image uploaded', 400
        
        file = request.files['image']
        if file.filename == '':
            logger.error("Empty filename")
            return 'No selected file', 400

        if not allowed_file(file.filename):
            logger.error(f"Invalid file type: {file.filename}")
            return 'File type not allowed', 400

        logger.info(f"Processing file: {file.filename}")

        try:
            # Read the image directly from the file stream
            img = Image.open(file.stream)
            logger.info(f"Image opened successfully. Format: {img.format}, Size: {img.size}, Mode: {img.mode}")

            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'P'):
                logger.info(f"Converting image from {img.mode} to RGB")
                img = img.convert('RGB')

            # Create output buffer
            output = io.BytesIO()
            
            # Save with compression
            logger.info("Saving compressed image...")
            img.save(output, format='JPEG', quality=50)
            output.seek(0)

            # Get the original filename and create a secure version
            original_filename = secure_filename(file.filename)
            compressed_filename = f'compressed_{original_filename}'
            
            logger.info(f"Sending compressed file: {compressed_filename}")
            
            return send_file(
                output,
                mimetype='image/jpeg',
                as_attachment=True,
                download_name=compressed_filename
            )

        except Exception as e:
            logger.error(f"Error processing image: {str(e)}")
            return str(e), 500

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True) 