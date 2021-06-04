from tkinter import *
from controller import registroController

root = Tk()
root.title("ScreenAI")
root.geometry("600x400")

    # Caja de texto central
root.columnconfigure(0, weight = 1, minsize = 75)
root.rowconfigure(0, weight = 1, minsize = 75)

texto = Label(root, text="Nombre")
texto.pack()
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
mensaje = Entry()
mensaje.pack(side="top")

texto = Label(root, text="Mail")
texto.pack()
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
mensaje = Entry()
mensaje.pack(side="top")

texto = Label(root, text="Password")
texto.pack()
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
mensaje = Entry()
mensaje.pack(side="top")


# Bucle de la apliación
root.mainloop()