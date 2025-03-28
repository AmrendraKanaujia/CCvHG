# CCvHG 
CCvHG - Cursor Control via Hand Gesture, a Python-based project that enables users to control the mouse cursor using hand gestures. This project utilizes OpenCV, MediaPipe, and PyAutoGUI to track hand movements and perform actions like left-click, right-click, scroll up and scroll down.

# Cursor Control via Hand Gesture

## Author
Amrendra Kumar Kanaujia (@amrendrakanaujia)

## Overview
This project allows users to control the cursor using hand gestures, leveraging computer vision and hand tracking technologies. It uses Python and various libraries like OpenCV, MediaPipe, and PyAutoGUI for gesture recognition and cursor automation.

## Features
- **Cursor Control:** Moves the cursor based on the index finger tip's position.
- **Left Click:** Performed when the index finger and thumb tip come close together.
- **Right Click:** Performed when the middle finger and thumb tip come close together.
- **Scroll Up:** Activated when the index and middle fingers are extended while the ring and little fingers are folded.
- **Scroll Down:** Activated when all fingers are folded except the thumb.
- **GUI Interface:** Built with Tkinter for user-friendly control.
- **Sound Feedback:** Uses Pygame to play sound on specific actions.

## Prerequisites
Ensure you have the following libraries installed:
```bash
pip install opencv-python mediapipe pyautogui pygame tkinter
```

## How to Use
1. **Start in a Neutral Position:** Keep your hand open with fingers extended.
2. **Launch the Application:** Run the Python script to start the GUI.
3. **Control the Cursor:** Use the defined gestures to move and click.
4. **Stop the Application:** Click the "Stop" button to exit safely.

## File Structure
```
- Source_Code/
  - ccvhgicon.ico    # Application icon
  - ccvhg_sound.mp3  # Click sound effect
  - main.py          # Main script with GUI and gesture control logic
```

## Known Issues
- **Hand out of Frame:** If the hand goes out of the camera frame, tracking may be lost.
- **Multiple Finger Movements:** Ensure only one functional gesture is performed at a time.
- **Lighting Conditions:** Works best in well-lit environments.

## Acknowledgments
Thanks to Python and its various libraries and tutorials that made this project possible.

