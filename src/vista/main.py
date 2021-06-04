
from tkinter import *
import os
from dotenv import main
import runpy
import importlib.util as imps


spec = imps.spec_from_file_location("mainController",os.path.join(os.path.dirname(__file__), "..\\controller\\mainController.py"))
mainController = imps.module_from_spec(spec)
spec.loader.exec_module(mainController)


vista = os.path.join(os.path.dirname(__file__), "usuario.py")



def herramientas():
     print("Herramientas")

def usuario():
    runpy.run_path(path_name=vista)

def configuracion():
    print("Configuracion")

def executeScript():
    mainController.execute(mensaje.get())

root = Tk()
root.title("ScreenAI")
root.geometry("500x400")
root.columnconfigure(0, weight = 1, minsize = 75)
root.rowconfigure(0, weight = 1, minsize = 75)
    # Menú superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_command(label="Herramientas", command=herramientas)
menubar.add_command(label="Usuario", command=usuario)
menubar.add_command(label="Configuracion", command=configuracion)
menubar.add_separator()
menubar.add_command(label="Salir", command=root.quit)

    # Caja de texto central
texto = Label(root, text="Introduzca comando")
texto.pack()
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

    # Monitor inferior
mensaje = Entry()
mensaje.pack(side="top")

bttn = Button(root, text="Introducir comando", command=executeScript)
bttn.pack()


root.config(menu=menubar)

# Bucle de la apliación
root.mainloop()