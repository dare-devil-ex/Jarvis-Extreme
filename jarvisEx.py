# Author: dare_devil_ex

import sys
from ddex.core.checker import DareDevilEx
from ddex.pyFixes.downloader import downloadPythonInstaller
import ddex.core.Mods.camera as clicks
from ddex.core.Mods.util import speak
downloadPythonInstaller()
DareDevilEx().checker()

import os, sys, datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import random
from pathlib import Path
import json
import pyautogui
import pyjokes

if sys.platform.startswith("win"):
    CONFIG_PATH = Path(r".\\ddex\\core\\config.json")
elif sys.platform.startswith("linux" ) or sys.platform.startswith("darwin"):
    CONFIG_PATH = Path(r"../Jarvis Extreme/ddex/core/config.json")

def wishes() -> None:
    """Greets the user based on the time of day."""
    speak("Welcome back, Homie!")
    print("Welcome back, Homie!")

    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good morning!")
        print("Good morning!")
    elif 12 <= hour < 16:
        speak("Good afternoon!")
        print("Good afternoon!")
    elif 16 <= hour < 24:
        speak("Good evening!")
        print("Good evening!")
    else:
        speak("Good night, see you tomorrow.")

    bot = load_name()
    speak(f"{bot} came back to online.")
    print(f"{bot} came back to online.")

def getTime() -> None:
    """Tells the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak("The current time is")
    speak(current_time)
    print("The current time is", current_time)

def getDate() -> None:
    """Tells the current date"""
    now = datetime.datetime.now()
    speak("The current date is")
    speak(f"{now.day} {now.strftime('%B')} {now.year}")
    print(f"The current date is {now.day}/{now.month}/{now.year}")

def screenshot() -> None:
    """Takes a screenshot and saves it."""
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\screenshot.png")
    img.save(img_path)
    speak(f"Screenshot saved as {img_path}.")
    print(f"Screenshot saved as {img_path}.")

def FecthCommands():
    """Takes microphone input from the user or falls back to text input."""
    r = sr.Recognizer()
    query = None
    mic_list = sr.Microphone.list_microphone_names()

    working_mic_index = None
    for i, mic_name in enumerate(mic_list):
        if "Microphone" in mic_name:
            working_mic_index = i
            break

    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        if json.load(f)["Author"] != "DareDevilEx":
            sys.exit("Unauthorized modification detected. Exiting...")
    if working_mic_index is None:
        return input("Type your command: ").lower()

    # Try listening from the mic
    try:
        with sr.Microphone(device_index=working_mic_index) as source:
            print(f"Listening using: {mic_list[working_mic_index]}")
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 1
            try:
                audio = r.listen(source, timeout=5)
            except sr.WaitTimeoutError:
                print("Timeout occurred. Please try again.")
                return input("Type your command: ").lower()

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return input("Type your command: ").lower()
        except sr.RequestError:
            print("Speech recognition service unavailable.")
            return input("Type your command: ").lower()
        except Exception as e:
            print(f"An error occurred: {e}")
            return input("Type your command: ").lower()

    except OSError as e:
        print(f"Microphone error ({e}). Falling back to text input.")
        return input("Type your command: ").lower()


def play_music(song_name=None) -> None:
    """Plays music from the user's Music directory."""
    song_dir = os.path.expanduser("~\\Music")
    songs = os.listdir(song_dir)

    if song_name:
        songs = [song for song in songs if song_name.lower() in song.lower()]

    if songs:
        song = random.choice(songs)
        os.startfile(os.path.join(song_dir, song))
        speak(f"Playing {song}.")
        print(f"Playing {song}.")
    else:
        speak("No song found.")
        print("No song found.")


def set_name() -> None:
    """Sets a new name for the assistant."""

    speak("What would you like to name me?")
    name = FecthCommands()

    if not name:
        speak("Sorry, I couldn't catch that.")
        return
    
    if CONFIG_PATH.exists():
        with CONFIG_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}

    data["botName"] = name
    with CONFIG_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    speak(f"Alright, I will be called {name} from now on.")

def selfie() -> None:
    """Takes a selfie using the webcam."""
    result = clicks.javrisSnapshot()
    if result:
        speak(result)

def load_name() -> str:
    """Loads the assistant's name from a file, or uses a default name"""

    if CONFIG_PATH.exists():
        with CONFIG_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"botName": "Jarvis Extreme"}

    return data["botName"]


def search_wikipedia(query):
    """Searches Wikipedia and returns a summary."""
    try:
        speak("Searching Wikipedia...")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
        print(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("Multiple results found. Please be more specific.")
    except Exception:
        speak("I couldn't find anything on Wikipedia.")


if __name__ == "__main__":
    wishes()

    while True:
        query = FecthCommands()
        if not query:
            continue

        if "time" in query:
            getTime()
            
        elif "date" in query:
            getDate()

        elif "wikipedia" in query:
            query = query.replace("wikipedia", "").strip()
            search_wikipedia(query)

        elif "play music" in query:
            song_name = query.replace("play music", "").strip()
            play_music(song_name)

        elif "open youtube" in query:
            wb.open("youtube.com")
            
        elif "open" in query:
            wb.open(query.split("open")[2] + ".com")

        elif "change your name" in query:
            set_name()

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif "shutdown" in query:
            speak("Shutting down the system, goodbye!")
            os.system("shutdown /s /f /t 1")
            break

        elif "set a selfie" in query or "take a selfie" in query or "click a selfie" in query:
            selfie()
            
        elif "restart" in query:
            speak("Restarting the system, please wait!")
            os.system("shutdown /r /f /t 1")
            break
            
        elif "offline" in query or "exit" in query or "q" in query:
            speak("Going offline. Have a good day!")
            break