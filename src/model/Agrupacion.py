class Agrupacion:
    def __init__(self, nombre, lista_scripts, autor, fecha_creacion, _id):
        self.nombre = nombre
        self.lista_scripts = lista_scripts
        self.autor = autor
        self.fecha_creacion = fecha_creacion
        self._id = _id

    def fill(self, nombre, lista_scripts, autor, fecha_creacion):
        self.nombre = nombre
        self.lista_scripts = lista_scripts
        self.autor = autor
        self.fecha_creacion = fecha_creacion

    #Setters
    def setId(self, _id):
        self._id = _id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setListaScripts(self, lista_scripts):
        self.lista_scripts = lista_scripts

    def setAutor(self, autor):
        self.autor = autor

    def setFechaCreacion(self, fecha_creacion):
        self.fecha_creacion = fecha_creacion     

    #Getters
    def getAll(self):
        return self

    def getId(self):
        return self._id

    def getNombre(self):
        return self.nombre 

    def getAutor(self):
        return self.autor

    def getFechaCreacion(self):
        return self.fecha_creacion

    def getListaScripts(self):
        return self.lista_scripts

    #Extras
    def addScript(self, script):
        self.lista_scripts.append(script)


