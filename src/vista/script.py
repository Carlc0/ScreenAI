from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
import os
import importlib.util as imps

spec = imps.spec_from_file_location("scriptController",os.path.join(os.path.dirname(__file__), "..\\controller\\scriptController.py"))
scriptController = imps.module_from_spec(spec)
spec.loader.exec_module(scriptController)

def nuevo():
    global ruta
    mensaje.set("Nuevo script")
    texto.delete(1.0, "end")
    root.title("Mi editor")

def abrir():
    ruta = ""
    mensaje.set("Abrir fichero")
    contenido = scriptController.abrir(ruta)
    if(contenido == ""):
        contenido = "Ha ocurrido un error al abrir el archivo"
    texto.delete(1.0,'end')
    texto.insert('insert', contenido)
    root.title(ruta + " - Mi editor")

def guardar():
    mensaje.set("Guardar fichero")
    contenido = texto.get(1.0,'end-1c')
    route = os.path.join(os.path.realpath('__file__'), ruta)
    route = os.path.abspath(os.path.realpath(route))
    fichero = open(route, 'w+')
    fichero.write(contenido)
    fichero.close()
    mensaje.set("Fichero guardado correctamente")

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

ruta = '../modules/extra/mod.py'

try:
    # Configuración de la raíz
    root = Tk()
    root.title("Mi editor")
    # Menú superior
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Nuevo", command=nuevo)
    filemenu.add_command(label="Abrir", command=abrir)
    filemenu.add_command(label="Guardar", command=guardar)
    filemenu.add_command(label="Guardar como", command=guardar_como)
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=root.quit)
    menubar.add_cascade(menu=filemenu, label="Archivo")
    # Caja de texto central
    texto = Text(root)
    texto.pack(fill="both", expand=1)
    texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))
    # Monitor inferior
    mensaje = StringVar()
    mensaje.set("Python script")
    monitor = Label(root, textvar=mensaje, justify='left')
    monitor.pack(side="left")
    root.config(menu=menubar)
    # Finalmente bucle de la apliación
    root.mainloop()

except Exception:
    print(Exception)