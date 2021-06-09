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
        route = os.path.join(os.path.realpath('__file__'), ruta)
        route = os.path.abspath(os.path.realpath(route))
        fichero = open(route, 'w+')
        fichero.write(script)
        fichero.close()
    except:
        print("error")