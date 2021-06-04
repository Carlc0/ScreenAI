class Usuario:
    def __init__(self, nombre, mail, contrasena, permiso, _id):
        self.mail = mail
        self.nombre = nombre
        self.contrasena = contrasena
        self.permiso = permiso
        self._id = _id

    def fill(self, nombre, mail, contrasena):
        self.mail = mail
        self.nombre = nombre
        self.contrasena = contrasena

    #Setters
    def setId(self, _id):
        self._id = _id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setMail(self, mail):
        self.mail = mail

    def setContrasena(self, contrasena):
        self.contrasena = contrasena

    def setPermiso(self, permiso):
        self.permiso = permiso     

    #Getters
    def getAll(self):
        return self

    def getId(self):
        return self._id

    def getNombre(self):
        return self.nombre

    def getMail(self):
        return self.mail

    def getContrasena(self):
        return self.contrasena

    def getPermiso(self):
        return self.permiso 
