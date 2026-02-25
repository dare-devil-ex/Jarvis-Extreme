# Author: dare_devil_ex

import cv2
import time
from PIL import Image

def javrisSnapshot() -> str | None:
    """Captures images from the webcam and saves them when 's' is pressed."""
    try:
        cap = cv2.VideoCapture(0)
    except Exception as e:
        return f"Error accessing the camera: {e}"

    if not cap.isOpened():
        print("Could not open camera")
        return "Could not open camera"

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow("DareDevilEX", frame)
        mills = int(time.time() * 1000)
        cv2.imwrite(f"JarvsExtreme_{mills}.jpg", frame)
        print(f"Image saved as JarvsExtreme_{mills}.jpg")
        time.sleep(0.2)
        print("Opening the saved image...")
        Image.open(f"JarvsExtreme_{mills}.jpg").show()
        return "How was the snapshot?"

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    javrisSnapshot()