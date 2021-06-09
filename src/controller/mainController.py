from os import walk
import runpy
from pyttsx3 import engine
from string import *


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

diccionario =  os.path.join(os.path.dirname(__file__), "..\\dicc\\commands.json\\")

core_modules = os.path.join(os.path.dirname(__file__), "..\\modules\\core\\")

extra_modules = os.path.join(os.path.dirname(__file__), "..\\modules\\extra\\")



def hablar():
    engine = pyttsx3.init()

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
        return {"ok":1, "error": Exception}

def speechrecog():
    hablar("Sistemas online. Introduzca comando: ")
    statement = escuchar()
    print(statement)
    #Error
    if statement["ok"]==1:
        raise Exception(statement["error"])


def execute(script):
    ret = False
    
    try:
        fin=""
        palabras = desglosar(script)
        if(palabras == False):
            raise Exception
        print(script)
        dicc = json.loads(diccionario)
        for comando in dicc.script:
            if(comando.accion == palabras[0] and comando.objeto == palabras[1]):
                fin = comando.archivo

        if(fin == ""): 
            raise Exception

        for(dirpath, dirnames, filenames) in os.walk(core_modules):
            if(filenames == fin and ret==False):
                runpy.run_path(path_name=os.path.join(core_modules, fin))
                ret=True
        if(ret==False):
            for(dirpath, dirnames, filenames) in os.walk(extra_modules):
                for elems in filenames:
                    if(elems == fin and ret==False):
                        runpy.run_path(path_name=os.path.join(extra_modules, fin))
                        ret=True
    except:
        print("Algo fue mal")
    finally:
        return ret

################### Funciones auxiliares ####################
def desglosar(comando):
    try:
        print(comando)
        return ["decir", "hola"]
    except:
        print("Error al parsear")
        return False