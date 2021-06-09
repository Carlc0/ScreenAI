import json
from tkinter import filedialog as Filedialog
from io import open
import os

diccionario = vista = os.path.join(os.path.dirname(__file__), "..\\dicc\\commands.json")#import del diccionario

ruta = '../modules/extra/'

def abrir():
    contenido = ""
    try:
        ruta = Filedialog.askopenfilename(#Funcion de Tk
            initialdir='.',
            filetypes=(("Script", "*.py"),),
            title="Abrir un script"
            )
        if ruta != "":
            fichero = open(ruta, 'r')
            contenido = fichero.read()
            fichero.close()
            if(contenido.count <= 0):
                raise Exception
    except:
        print(Exception)
    finally:
        return contenido

def guardar(script, nombre, accion, objeto):
    try:
        dicc = json.loads(diccionario)
        for script in dicc.script:
            if(script.accion == accion and script.objeto == objeto):
                

        route = os.path.join(os.path.realpath('__file__'), ruta)
        route = os.path.abspath(os.path.realpath(route))
        fichero = open(route, 'w+')
        fichero.write(script)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    except:


def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero",
        mode="w", defaultextension=".py")
    if fichero is not None:
        ruta = fichero.name
        print(ruta)
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
        root.quit
    else:
        mensaje.set("Guardado cancelado")

