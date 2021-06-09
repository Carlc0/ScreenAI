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
    dicc = ""
    try:
        with open(diccionario, 'r') as file:
            dicc = json.loads(open(diccionario, "r").read())
            
        for comando in dicc["script"]:
            if(comando["accion"] == accion and comando["objeto"] == objeto):
                raise Exception
        route = os.path.join(os.path.realpath('__file__'), ruta+nombre+".py")
        route = os.path.abspath(os.path.realpath(route))
        print(route)
        fichero = open(route, 'w')
        fichero.write(script)
        fichero.close()
        print("caca")
        dicc["accion"].append(accion)
        dicc["objeto"].append(objeto)
        dicc["scripts"].append({"accion":accion,"objeto":objeto,"script":nombre+".py"})
        print(dicc)
        nuevoDicc = open(diccionario, 'w+')
        nuevoDicc.write(dicc)
        nuevoDicc.close()
    except:
        print("error")