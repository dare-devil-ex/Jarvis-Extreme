# Author: dare_devil_ex

import os
import sys

class DareDevilEx:
    packages = [
        "pyttsx3",
        "wikipedia",
        "SpeechRecognition==3.8.1",
        "PyAutoGUI",
        "pywintypes",
        "setuptools",
        "sounddevice",
        "opencv-python",
        "wget",
        "pyjokes"
    ]
    
    def checker(self) -> None:
        for pkg in self.packages:
            try:
                __import__(pkg.lower() if pkg != "SpeechRecognition==3.8.1" else "speech_recognition")
                os.system("cls" if sys.platform.startswith("win") else "clear")
            except:
                print(f"Installing {pkg}...")
                os.system(f"python -m pip install {pkg}")
                os.system("cls" if sys.platform.startswith("win") else "clear")