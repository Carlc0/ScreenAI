
from tkinter import *
from controller.mainController import *

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