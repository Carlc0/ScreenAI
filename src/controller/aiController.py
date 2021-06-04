from pyttsx3 import engine


try:
    from tkinter import *
    import threading
    import pyttsx3
    import os
    import subprocess
    import webbrowser
    import time
    import json
    import requests
    import speech_recognition as sr
    from io import open
    from pymongo import MongoClient
    from dotenv import load_dotenv
except Exception:
    print("Error: library not found")
    exit()

engine = pyttsx3.init()

def hablar(texto):
    print(texto)
    engine.say(texto)
    engine.runAndWait()


def escuchar():
    try:
        r = sr.Recognizer() 
        with sr.Microphone() as source:
            print (sr.Microphone.list_microphone_names())
            raw = r.listen(source)
            ret = r.recognize_google(raw, languaje='in-en')
            return ret
    except Exception:
        print(Exception.args)
        return json.dump({"ok":1, "error": Exception})