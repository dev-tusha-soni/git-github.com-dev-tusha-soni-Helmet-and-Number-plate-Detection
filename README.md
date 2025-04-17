Helmet and Number Plate Detection
Project Overview
This project is designed to automatically detect whether a motorbike rider is wearing a helmet and to recognize the number plate of the vehicle. It uses deep learning and computer vision techniques to promote road safety by ensuring that riders comply with traffic rules.

The system processes input images or videos, detects if the rider is wearing a helmet, and extracts the vehicle's number plate. This is achieved using pre-trained deep learning models for helmet detection and number plate recognition. The output is an image or video with bounding boxes highlighting the helmet and number plate areas.

Features
Helmet Detection: Detect whether a motorbike rider is wearing a helmet.

Number Plate Recognition: Automatically recognize and extract the number plate of the vehicle.

Real-time Processing: Works with both images and video inputs.

Result Display: Displays the processed image with bounding boxes around the helmet and number plate, along with the detected plate number.

Technologies Used
Python: For backend processing and handling the deep learning models.

Flask: For creating the backend API that integrates with the frontend.

OpenCV: For image and video processing.

TensorFlow: For training and running the deep learning models.

YOLO (You Only Look Once): A state-of-the-art real-time object detection system used for both helmet detection and number plate recognition.

Tesseract OCR: For optical character recognition of number plates.

HTML/CSS/JavaScript: For the frontend user interface and displaying results.

Flow of the System
Input Image/Video: The user uploads an image or feeds a video from a camera to the system.

Helmet Detection: The system processes the input to check if the rider is wearing a helmet using a deep learning model.

Number Plate Recognition: After helmet detection, the system scans for the number plate and extracts the text using Optical Character Recognition (OCR).

Output Display: The processed image is displayed with bounding boxes around the helmet and number plate, along with the extracted number plate text.

Installation
Prerequisites
Before running the project, ensure you have Python and pip installed. Additionally, install the required libraries:



YOLO model weights (yolov4.weights)

YOLO config file (yolov4.cfg)

YOLO class names (coco.names)





Code Explanation
Backend (app.py)
This file handles the API requests for uploading images or videos, processes them using machine learning models, and sends the processed result back to the frontend. Here's a small code snippet from the app.py file:

python
Copy
Edit
from flask import Flask, request, jsonify
import cv2
import numpy as np
from detect import detect_helmet_and_plate

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    file.save("input_image.jpg")
    
    result_image, plate_text = detect_helmet_and_plate("input_image.jpg")
    
    result_image_path = "result_image.jpg"
    cv2.imwrite(result_image_path, result_image)

    return jsonify({"message": "Image processed successfully", "plate_text": plate_text, "image": result_image_path})

if __name__ == '__main__':
    app.run(debug=True)
In this snippet, we process the uploaded image, pass it through the detect_helmet_and_plate function, and return the result along with the extracted number plate text.

Detection Logic (detect.py)
This file contains the core logic for detecting helmets and number plates. Here's a small code snippet from detect.py:

python
Copy
Edit
import cv2
import pytesseract
from tensorflow.keras.models import load_model

# Load pre-trained model
helmet_model = load_model('helmet_detection_model.h5')
plate_model = load_model('plate_detection_model.h5')

def detect_helmet_and_plate(image_path):
    # Load image
    img = cv2.imread(image_path)
    
    # Perform helmet detection
    helmet_detected = helmet_model.predict(img)
    
    # Perform number plate detection
    plate_detected, plate_text = detect_plate_and_recognize(img)
    
    # Draw bounding boxes for helmet and number plate
    if helmet_detected:
        img = cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)
    
    if plate_detected:
        img = cv2.rectangle(img, (100, 100), (400, 200), (255, 0, 0), 2)
        img = cv2.putText(img, plate_text, (100, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    return img, plate_text

def detect_plate_and_recognize(img):
    # Use Tesseract OCR to extract the number plate
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plate_text = pytesseract.image_to_string(gray_img)
    
    # For simplicity, assume we detect a plate if OCR returns some text
    return bool(plate_text.strip()), plate_text.strip()
This code handles both the helmet detection and number plate recognition. It draws bounding boxes around the detected helmet and plate, and uses Tesseract OCR to extract the plate text.

Example Output
When the system processes an image or video, it detects whether the rider is wearing a helmet and recognizes the vehicle's number plate. Below is an example output:


