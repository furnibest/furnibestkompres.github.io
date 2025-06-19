# Image Compressor

A simple web application that allows you to compress images using Python and Flask.

## Features

- Drag and drop interface for image upload
- Image preview before compression
- Automatic image compression
- Support for various image formats
- Modern and responsive UI

## Requirements

- Python 3.7 or higher
- Flask
- Pillow (PIL)

## Installation

1. Clone this repository or download the files
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```bash
   python app.py
   ```
2. Open your web browser and go to `http://localhost:5000`
3. Drag and drop an image or click to select one
4. Click the "Compress Image" button
5. The compressed image will be downloaded automatically

## How it works

The application uses the Pillow library to compress images while maintaining reasonable quality. The compression is done by:

1. Converting images to RGB format if necessary
2. Optimizing the image using JPEG compression
3. Setting the quality to 50% (this can be adjusted in the code)

## License

This project is open source and available under the MIT License. 