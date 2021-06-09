from tkinter import *

rooter = Tk()
rooter.title("ScreenAI")
rooter.geometry("600x400")

    # Caja de texto central
rooter.columnconfigure(0, weight = 1, minsize = 75)
rooter.rowconfigure(0, weight = 1, minsize = 75)

texto = Label(rooter, text="Nombre")
texto.pack()
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
nombre = Entry(rooter)
nombre.pack(side="top")

texto = Label(rooter, text="Mail")
texto.pack()
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
mail = Entry(rooter)
mail.pack(side="top")

texto = Label(rooter, text="Password")
texto.pack()
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
contrasena = Entry(rooter)
contrasena.pack(side="top")

bttn = Button(rooter, text="log in")
bttn.pack()
bttn = Button(rooter, text="registrarse")
bttn.pack()


# Bucle de la apliación
rooter.mainloop()