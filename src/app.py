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
    engine.say(texto)
    engine.runAndWait()


def escuchar():
    esc = sr.Recognizer() 
    with sr.Microphone() as source:
        raw = esc.listen(source)
        try:
            ret = esc.recognize_google(raw, languaje='es')
            return {"ok":0, "return":ret}
        except Exception:
            return {"ok":1, "error": Exception}
    sr.listen()
        
##
# Main function
# 

    
exit = False
try:
    while (exit==False):
        print("itereacion")
        hablar("Sistema online. Introduzca comando: ")
        statement = escuchar()
        #Error
        if statement.ok==1:
            print("Error: "+statement.error)
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
except:
    print('Error inesperado')