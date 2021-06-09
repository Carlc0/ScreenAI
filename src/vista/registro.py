import runpy
from tkinter import *
import os
import sys
import tkinter
from pymongo import MongoClient
import hashlib
import os
import json
import importlib.util as imps

main = os.path.join(os.path.dirname(__file__), "main.py")
logo = os.path.join(os.path.dirname(__file__), "..\\imgs\\logo.png")#import de logo

spec = imps.spec_from_file_location("registroController",os.path.join(os.path.dirname(__file__), "..\\controller\\registroController.py"))
registroController = imps.module_from_spec(spec)
spec.loader.exec_module(registroController)

client = MongoClient("mongodb://localhost:27017")
db = client.ScrenAi

def registrer():
    ret=True
    try:

        user = json.dumps({"nombre": nombre.get(), "mail":mail.get(), "contrasena":contrasena.get()})

        user = registroController.registro(user)

        if(user == False): raise Exception
    except:
        print("Something went wrong")

def logein(user):
    ret=True
    try:
        
        user = json.dumps({"mail":mail.get(), "contrasena":contrasena.get()})

        posts = db.usuarios

        inserted = posts.find_one(user)

        runpy.run_path(path_name=main)

        if(inserted == 'null'):
            ret = False
    except:
        ret = False
    finally:
        return ret

root = Tk()
root.title("ScreenAI")
root.geometry("600x400")
root.iconphoto(True, tkinter.PhotoImage(file=logo))

    # Caja de texto central
root.columnconfigure(0, weight = 1, minsize = 75)
root.rowconfigure(0, weight = 1, minsize = 75)

texto = Label(root, text="Nombre")
texto.pack()
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
nombre = Entry()
nombre.pack(side="top")

texto = Label(root, text="Mail")
texto.pack()
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
mail = Entry()
mail.pack(side="top")

texto = Label(root, text="Password")
texto.pack()
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
contrasena = Entry()
contrasena.pack(side="top")

bttn = Button(text="log in", command=logein)
bttn.pack()
bttn = Button(text="registrarse", command=registrer)
bttn.pack()


# Bucle de la apliación
root.mainloop()