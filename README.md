

# Hand Gesture Mouse Control

This project uses Python libraries such as `OpenCV`, `MediaPipe`, and `PyAutoGUI` to control the mouse cursor using hand gestures. It specifically tracks the index finger and thumb to move the cursor and perform click actions.

## Requirements

- Python 3.8.10 only
- `opencv-python`
- `mediapipe`
- `pyautogui`

You can install the required dependencies using `pip`:

```bash
pip install opencv-python mediapipe pyautogui
```

## How It Works

1. **Hand Detection**: The program uses MediaPipe's hand tracking solution to detect hand landmarks, focusing on the index finger and thumb.
2. **Cursor Movement**: The program tracks the movement of the index finger and uses its coordinates to move the mouse cursor on the screen.
3. **Clicking**: When the distance between the index finger and thumb becomes small (indicating a pinching gesture), it triggers a mouse click.

## Features

- Real-time hand detection and tracking.
- Cursor movement controlled by the index finger position.
- Mouse clicking triggered by a "pinch" gesture (index finger and thumb close together).

## Usage

1. **Run the script**:
   Simply run the Python script in a terminal or IDE.

   ```bash
   python main.py
   ```

2. **Positioning the hand**:
   - Your hand should be in the camera frame.
   - Move your index finger to control the mouse cursor.
   - Perform a pinching gesture (bring index finger and thumb close) to simulate a mouse click.

## Notes

- The script uses the computer's webcam, so make sure it is working and accessible.
- The screen size is automatically adjusted based on your screen resolution.

## Troubleshooting

- **No detection of hands**: Ensure that your camera is on and that your hands are visible in the frame.
- **Cursor not moving smoothly**: The cursor movement is directly related to the position of your hand's index finger. Ensure the frame has good lighting and the hand is clearly visible.
- **Click not triggering**: The script uses a fixed distance (20 pixels) between the thumb and index finger for detecting clicks. This threshold may need adjustment depending on hand size or camera distance.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

