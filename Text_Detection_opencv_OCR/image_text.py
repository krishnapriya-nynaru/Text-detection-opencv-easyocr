import easyocr
import cv2
import numpy as np
import argparse
import os
import sys

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

# Argument parser for command line arguments
parser = argparse.ArgumentParser(description="OCR using EasyOCR with image, video, or webcam.")
parser.add_argument('--mode', type=str, required=True, choices=['image', 'video', 'webcam'],
                    help="Choose mode: 'image', 'video', or 'webcam'")
parser.add_argument('--path', type=str, help="Path to image or video file (optional). Defaults to 'test_images' for image or 'test_videos' for video.")

# Correct method to parse arguments
args = parser.parse_args()

# Default directories for image and video
default_image_dir = 'test_images'
default_video_dir = 'test_videos'

# Function to perform OCR on an image
def perform_ocr(frame):
    result = reader.readtext(frame)
    font = cv2.FONT_HERSHEY_SIMPLEX

    for detection in result:
        top_left = tuple(map(int, detection[0][0]))
        bottom_right = tuple(map(int, detection[0][2]))
        text = detection[1]
        frame = cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
        frame = cv2.putText(frame, text, (top_left[0], top_left[1] - 10), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

    return frame

# Mode: Image
if args.mode == 'image':
    # If no path is provided, use the default 'test_images' folder
    image_path = args.path if args.path else os.path.join(default_image_dir, 'test_image.jpg')

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not open image at {image_path}.")
        sys.exit()

    # Perform OCR
    processed_image = perform_ocr(image)

    # Display the image with OCR results
    cv2.imshow("Image OCR", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Mode: Video
elif args.mode == 'video':
    # If no path is provided, use the default 'test_videos' folder
    video_path = args.path if args.path else os.path.join(default_video_dir, 'test_video.mp4')

    # Load the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video at {video_path}.")
        sys.exit()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform OCR
        processed_frame = perform_ocr(frame)

        # Display the frame with OCR results
        cv2.imshow("Video OCR", processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Mode: Webcam
elif args.mode == 'webcam':
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        sys.exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image from webcam.")
            break

        # Perform OCR
        processed_frame = perform_ocr(frame)

        # Display the frame with OCR results
        cv2.imshow("Webcam OCR", processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
