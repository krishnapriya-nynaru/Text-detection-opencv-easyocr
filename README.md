# Text-detection-opencv-easyocr
This project demonstrates how to perform Optical Character Recognition (OCR) using the EasyOCR library in three modes: image, video, and webcam. With this script, you can extract text from static images, videos, or even real-time webcam streams. The recognized text is displayed over the input with bounding boxes using OpenCV for visualization.

#### Key Features
**Image OCR:** Extracts text from image files.

**Video OCR:** Extracts text frame-by-frame from a video.

**Webcam OCR:** Uses your webcam to capture live video and extract text in real-time.

**EasyOCR:** A deep learning-based OCR library that supports multiple languages and provides highly accurate text recognition.

### Table of Contents
- Introduction
- Technologies
- Installation
- Usage
- Arguments
- Results
- Acknowledgements

## Introduction
**Optical Character Recognition (OCR)** is the process of converting different types of documents, such as scanned paper documents, PDF files, or images, into editable and searchable data. In this project, we use the EasyOCR library, which is a deep learning-based OCR solution with support for over 80 languages.

Using this project, you can choose to extract text from an image file, process a video for text detection, or utilize your system’s webcam for live text recognition. The recognized text will be displayed over the original media with bounding boxes, making it easy to visualize where the text is located.

## Technologies
**Python:** Primary language for building this OCR tool.

**EasyOCR:** A popular OCR library based on deep learning, supporting many languages.

**OpenCV:** Used for image and video processing, including drawing bounding boxes around detected text and handling media inputs (image, video, and webcam).

## Installation
- Clone the repository:
    ```bash
    git clone https://github.com/krishnapriya-nynaru/Text-detection-opencv-easyocr.git
- Install required packages :
    ```bash
    pip install -r requirements.txt
- Change to project directory
    ```bash
    cd Text_Detection_opencv_OCR
## Usage
Run the script with Python, specifying the mode of operation as image, video, or webcam.

**Command Line Arguments:**

- --mode: Required. Choose one of the following:
    - image: Perform OCR on an image file.
    - video: Perform OCR on a video file.
    - webcam: Perform OCR using the webcam.
- --path: Optional. Path to the image or video file. If not provided, the default directories test_images/ or test_videos/ will be used.
#### Examples:
**Image Mode**

    python image_text.py --mode image --path path/to/your/image.jpg
If no path is provided, it defaults to test_images/test_image.jpg.

**Video Mode**

    python ocr_script.py --mode video --path path/to/your/video.mp4
If no path is provided, it defaults to test_videos/test_video.mp4.

**Webcam Mode**

    python ocr_script.py --mode webcam
This opens your default webcam and performs real-time OCR.

## Arguments
- **--mode:** Specifies the operation mode:
    - image: Performs OCR on a single image file.
    - video: Performs OCR on a video file.
    - webcam: Performs OCR on a live video feed from your webcam.
- **--path:**
(Optional) Specifies the path to the input file (image or video). If no path is provided, the program will default to using a test image or video from the test_images/ or test_videos/ directories.

## Acknowledgements
[**EasyOCR:**](https://github.com/JaidedAI/EasyOCR) A powerful OCR library that supports over 80 languages.

[**OpenCV:**](https://opencv.org/) A popular computer vision library used for video and image processing.
