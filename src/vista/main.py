
from tkinter import *
from tkinter import messagebox
import os
import tkinter
from dotenv import main
import runpy
import importlib.util as imps


spec = imps.spec_from_file_location("mainController",os.path.join(os.path.dirname(__file__), "..\\controller\\mainController.py"))
mainController = imps.module_from_spec(spec)
spec.loader.exec_module(mainController)

vista = os.path.join(os.path.dirname(__file__), "usuario.py")#import de vista
script = os.path.join(os.path.dirname(__file__), "script.py")#import de script
logo = os.path.join(os.path.dirname(__file__), "..\\imgs\\logo.png")#import de script


def reconsComms():
    print("Herramientas")

def nuevoComm():
    runpy.run_path(path_name=script)

def usuario():
    runpy.run_path(path_name=vista)

def configuracion():
    print("Configuracion")

def executeScript():
    if(mainController.execute(mensaje.get())==False):
        consola.set(consola.get()+"\nComando no reconocido")

root = Tk()
root.title("ScreenAI")
root.geometry("500x200")
root.iconphoto(True, tkinter.PhotoImage(file=logo))
root.columnconfigure(0, weight = 1, minsize = 75)
root.rowconfigure(0, weight = 1, minsize = 75)
# Menú superior
menubar = Menu(root)
#Menu herramientas
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Implementar nueva funcionalidad", command=nuevoComm)
filemenu.add_command(label="Reconstruir arbol de comandos", command=reconsComms)
menubar.add_cascade(menu=filemenu, label="Herramientas")
menubar.add_command(label="Usuario", command=usuario)
menubar.add_command(label="Configuracion", command=configuracion)
menubar.add_separator()
menubar.add_command(label="Salir", command=root.quit)

# Caja de texto central
consola = StringVar()
consola.set("Bienvenido a ScreenAi")
texto = Label(textvariable=consola)
texto.pack()
texto.config(bd=1, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
mensaje = Entry()
mensaje.pack(side="top")

bttn = Button(root, text="Introducir comando", command=executeScript)
bttn.pack()


root.config(menu=menubar)

mainController.hablar("ScreenAi operativo, introduzca comando")

# Bucle de la aplicación
root.mainloop()

