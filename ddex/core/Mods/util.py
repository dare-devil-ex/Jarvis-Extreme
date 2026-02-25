from typing import Any
import pyttsx3

engine = pyttsx3.init()
voices_index = 0    # 0: Female | 1: Male
voices: Any = engine.getProperty('voices')
engine.setProperty('voice', voices[voices_index].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

def speak(audio) -> None:
    engine.say(audio)
    engine.runAndWait()