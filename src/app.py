#Imports
try:
    import pyttsx3
    import os
    import subprocess
    import webbrowser
    import time
    import json
    import requests
    import speech_recognition as sr
    from dotenv import load_dotenv
except Exception:
    print("Error: library not found")
    print(Exception)


#Inicializador de reconocimiento de voz
engine = pyttsx3.init()

##
#  Funcion decir cosas por el 
#  
def hablar(texto):
    print(texto)
    engine.say(texto)
    engine.runAndWait()


def escuchar():
    try:
        esc = sr.Recognizer() 
        with sr.Microphone() as source:
            raw = esc.listen(source)
            ret = esc.recognize_google(raw, languaje='in-en')
            return {"ok":0, "ret":ret}
    except Exception:
        print(Exception)
        return {"ok":1, "error": Exception}
        
##
# Main function
# 
exit = False
try:
    while (exit==False):
        print("itereacion")
        hablar("Yamarashi online. Introduzca comando: ")
        statement = escuchar()
        print(statement)
        #Error
        if statement["ok"]==1:
            raise Exception(statement["error"])
        #Salir
        elif "parar programa" in statement.ret:
            hablar('Sistema offline. Adios')
            exit = True
        
        #
        elif 'abrir youtube' in statement.ret:
            webbrowser.open_new_tab("https://www.youtube.com")
            time.sleep(5)
        #
        elif 'abrir google' in statement.ret:
            webbrowser.open_new_tab("https://www.google.com")
            time.sleep(5)
            
        #
        elif 'abrir gmail' in statement.ret:
            webbrowser.open_new_tab("gmail.com")
            time.sleep(5)
            
        #
        elif "apagar ordenador" in statement.ret:
            hablar("Apagando Ordenador")
            subprocess.call(["shutdown", "/l"])
except Exception:
    print(Exception.with_traceback)