# Face Detection System

This project is a face detection system using Haar cascades and OpenCV. It captures images from an IP camera, processes them, and detects faces.

## Project Structure

The project consists of the following scripts:
- `collect_data.py`: Captures images from the IP camera.
- `consolidated_data.py`: Organizes and preprocesses the collected image data.
- `face_detect.py`: Uses the Haar cascade to detect faces in the images.
- `recognize.py`: Recognizes faces from the detected face regions.

## Requirements

- Python 3.10
- OpenCV
- NumPy

## Folder Structure

```
Face-Detection-System/
├── README.md                     # Project Documentation
├── haarcascade_frontalface.xml
├── collect_data.py
├── consolidated_data.py
├── face_detect.py
├── recognize.py
├── data/                         # After preprocessing the collected data, this folder is automatically generated.
└── images/                       # After collecting data from your IP camera, this folder is automatically generated.
```

    

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Nishantdas77/face-detection.git
   cd face-detection
2. Install the required packages:
   ```sh
   pip install opencv-python numpy
3. IP Camera Configuration:
   ```sh
   Ensure you replace the IP camera URL in the scripts with your own IP camera URL.
4. Collecting Data:
   ```sh
   python collect_data.py
5. Consolidating Data:
   ```sh
   python consolidated_data.py
6. Detecting Faces:
   ```sh
   python face_detect.py
7. Recognizing Faces:
   ```sh
   python recognize.py

## Contact

If you have any questions, feedback, or inquiries, feel free to reach out:

- **Name:** [Nishant Kumar Das]
- **Email:** [dasnishant7777@gmail.com]
- **GitHub:** [https://github.com/Nishantdas77](https://github.com/Nishantdas77)

We appreciate your interest in our project and look forward to hearing from you!


