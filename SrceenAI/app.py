#Imports
import pyttsx3
import os
import subprocess
import webbrowser
import time
import json
import requests

#Inicializador de reconocimiento de voz
engine = pyttsx3.init()

##
#  Funcion decir cosas por el 
#  
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

##
# Main function
# 
if __name__=='__main__':
    exit = False
    try:
        while (exit==False):
            hablar("Sistema online. Introduzca comando: ")
            statement = ''

            #Error
            if statement.count==0:
                print('Error')

            #Salir
            elif "adios" in statement or "salir" in statement or "parar" in statement:
                hablar('Sistema offline. Adios')
                exit = True
            
            #
            elif 'abrir youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                time.sleep(5)

            #
            elif 'abrir google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                time.sleep(5)
                
            #
            elif 'abrir gmail' in statement:
                webbrowser.open_new_tab("gmail.com")
                time.sleep(5)
                
            #
            elif "log off" in statement or "sign out" in statement:
                hablar("Apagando Ordenador")
                subprocess.call(["shutdown", "/l"])
    except:
        print('Error inesperado')