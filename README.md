Face Webcam Detection.
A Python-based project for real-time detection of faces, eyes, and smiles using OpenCV. This project demonstrates how to use Haar Cascade classifiers for facial feature detection in both static images and live webcam feeds.
Features
Real-time detection of:
Faces: Highlighted with a blue rectangle.
Eyes: Highlighted with green rectangles.
Smiles: Highlighted with red rectangles.
User-friendly and lightweight script for local execution.

Installation
Follow these steps to run the project locally:

Clone the Repository:

bash
git clone https://github.com/TaufiaHussain/Face-webcam-Detection.git

Install Dependencies:

Ensure Python is installed on your system.
Install the required library.
pip install opencv-python

Run the Script:

Open a terminal or command prompt.
Navigate to the project folder.
cd Face-webcam-Detection
cd Face-webcam-Detection

Run the detection script:
python webcam_detection.py

Files in the Repository
webcam_detection.py: Script for real-time detection using the webcam.
face_eye_and_smile_detection.py: Script for detecting faces, eyes, and smiles in static images.

How It Works
Detection Framework:

The scripts utilize OpenCV’s pre-trained Haar Cascade classifiers for detecting:
Faces
Eyes
Smiles
Real-Time Processing:

Webcam frames are captured in real-time, converted to grayscale, and passed through the classifiers.
Bounding Boxes:

Detected features are highlighted:
Blue: Face
Green: Eyes
Red: Smile

Technologies Used
Python: Core programming language.
OpenCV: Library for image and video processing.

Contributing
Contributions are welcome! Here’s how you can contribute:

Fork the repository.
Create a feature branch:
git checkout -b feature-name

git commit -m "Add feature or fix issue"

git push origin feature-name

License:

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments:

OpenCV Documentation: For pre-trained Haar Cascades and tutorials.
Thanks to contributors and users for their valuable feedback.
