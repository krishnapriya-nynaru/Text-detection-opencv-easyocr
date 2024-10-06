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
- Examples
- Acknowledgements

### Introduction
**Optical Character Recognition (OCR)** is the process of converting different types of documents, such as scanned paper documents, PDF files, or images, into editable and searchable data. In this project, we use the EasyOCR library, which is a deep learning-based OCR solution with support for over 80 languages.

Using this project, you can choose to extract text from an image file, process a video for text detection, or utilize your system’s webcam for live text recognition. The recognized text will be displayed over the original media with bounding boxes, making it easy to visualize where the text is located.

#### Technologies
**Python:** Primary language for building this OCR tool.

**EasyOCR:** A popular OCR library based on deep learning, supporting many languages.

**OpenCV:** Used for image and video processing, including drawing bounding boxes around detected text and handling media inputs (image, video, and webcam).
