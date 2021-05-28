#Imports
from speech_recognition import Microphone


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
    from tkinter import filedialog as FileDialog
    from io import open
    from pymongo import MongoClient
    from dotenv import load_dotenv
except Exception:
    print("Error: library not found")
    exit()


#Inicializador de reconocimiento de voz
engine = pyttsx3.init()

ruta = ""

##
#  Funcion decir cosas por el 
#  
def hablar(texto):
    print(texto)
    engine.say(texto)
    engine.runAndWait()


def escuchar():
    try:
        r = sr.Recognizer() 
        with sr.Microphone() as source:
            print (Microphone.list_microphone_names())
            raw = r.listen(source)
            ret = r.recognize_google(raw, languaje='in-en')
            return ret
    except Exception:
        print(Exception.args)
        return {"ok":1, "error": Exception}

def escribir():
    try:
        print("escribir")
    except Exception:
        print(Exception.args)
        return {"ok":1, "error": Exception}
        
def herramientas():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor")

def usuario():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(("Ficheros de texto", "*.txt"),),
        title="Abrir un fichero de texto")
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")

def configuracion():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")

def dirs():
    if(os.path.exists(os.path.join('modules/extra', '.py'))):
        for files in os.walk('modules/extra'):
            print("Files: "+files)

##
# Main function
# 
exit = False
try:
    root = Tk()
    root.title("ScreenAI")
    root.geometry("500x400")
    # Menú superior
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_command(label="Herramientas", command=herramientas)
    menubar.add_command(label="Usuario", command=usuario)
    menubar.add_command(label="Configuracion", command=configuracion)
    menubar.add_separator()
    menubar.add_command(label="Salir", command=root.quit)

    # Caja de texto central
    texto = Label(root)
    texto.grid(row=10, column=50)
    texto.pack()
    texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

    # Monitor inferior
    mensaje = Entry()
    mensaje.pack(side="left")


    root.config(menu=menubar)

    # Bucle de la apliación
    root.mainloop()

    dirs()

    while (exit==False):
        print("itereacion")
        hablar("Sistemas online. Introduzca comando: ")
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
    print("Fallo en Main")