Rock-Paper-Scissors Game with Hand Gesture Recognition

This is a Python-based Rock-Paper-Scissors game that uses computer vision to recognize hand gestures from two players in real-time. The game utilizes OpenCV for video capture and display, and MediaPipe for hand detection and gesture recognition.

Table of Contents

	•	Features
	•	Prerequisites
	•	Installation
	•	Usage
	•	Hand Gestures
	•	Troubleshooting
	•	License
	•	Acknowledgements

Features

	•	Real-time Gesture Recognition: Detects hand gestures for Rock, Paper, and Scissors using a webcam.
	•	Two-Player Mode: Allows two players to compete against each other with score tracking.
	•	Visual Feedback: Displays recognized gestures, player scores, and game results on the screen.
	•	User-Friendly Interface: Easy to set up and play with on-screen instructions.

Prerequisites

	•	Python 3.x
	•	Webcam: Built-in or external webcam for video capture.

Installation

	1.	Clone the Repository

git clone https://github.com/yourusername/rock-paper-scissors-gesture.git
cd rock-paper-scissors-gesture


	2.	Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


	3.	Install Required Packages

pip install opencv-python mediapipe



Usage

	1.	Connect Your Webcam
Ensure your webcam is properly connected and recognized by your computer.
	2.	Run the Script

python rock_paper_scissors.py


	3.	Enter Player Names
When prompted, enter names for Player 1 and Player 2.
	4.	Play the Game
	•	Position your hands so they are clearly visible to the webcam.
	•	Make a gesture representing Rock, Paper, or Scissors.
	•	The game will recognize the gestures and display the result.
	•	Scores are updated after each round.
	•	Press ‘q’ at any time to quit the game.

Hand Gestures

	•	Rock
	•	Gesture: All fingers closed into a fist.
	•	How to Make: Close your hand into a fist with the thumb over the fingers.
	•	Paper
	•	Gesture: All fingers extended and spread out.
	•	How to Make: Open your hand fully with fingers spread apart.
	•	Scissors
	•	Gesture: Only the index and middle fingers extended.
	•	How to Make: Extend your index and middle fingers to form a ‘V’ shape, while keeping the other fingers closed.

Troubleshooting

	•	Camera Not Detected
	•	Ensure your webcam is connected and functioning.
	•	If using an external camera, try changing the camera index in the code:

camera = cv2.VideoCapture(0)

Change 0 to 1 or another index if necessary.

	•	Poor Gesture Recognition
	•	Use a well-lit environment to improve detection accuracy.
	•	Ensure your hand is fully within the camera frame and not too close or too far.
	•	Avoid complex backgrounds that might confuse the hand detection.
	•	Module Not Found Error
	•	Ensure all dependencies are installed correctly:

pip install opencv-python mediapipe


	•	Verify that you are using the correct Python environment.

	•	Script Crashes or Freezes
	•	Check for any error messages in the terminal and address them accordingly.
	•	Ensure your computer meets the minimum requirements to run OpenCV and MediaPipe.

License

This project is licensed under the MIT License.

Acknowledgements

	•	OpenCV - Open Source Computer Vision Library.
	•	MediaPipe - Cross-platform machine learning solutions for live and streaming media.
