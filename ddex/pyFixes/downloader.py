# Author: dare_devil_ex

import os
from wget import download
import sys, os

baseUrl = "https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe"

def downloadPythonInstaller():
    """To install the stable version of the Python, which had prebuilt PyAudio"""

    if sys.version.split()[0] != "3.11.9":
        print(f"Warning: You are using Python {sys.version.split()[0]}, but this project requires Python 3.11.9.")

        if input("Do you want to download Python 3.11.9 installer? (y/n): ").lower() == 'y':
            print(f"Downloading Python installer from {baseUrl}...")

            download(baseUrl, "./ddex/pyFixes/python-3.11.9-amd64.exe")
            print("Download completed. Please run the installer manually.")

            if sys.platform.startswith("win"):
                os.startfile(os.getcwd() + "\\ddex\\pyFixes\\")
            elif sys.platform.startswith("linux"):
                os.system(os.getcwd() + '/ddex/pyFixes/')
            elif sys.platform.startswith("darwin"):
                os.system(os.getcwd() + '/ddex/pyFixes/')
            else:
                print("Please navigate to the ddex/pyFixes/ directory to run the installer.")