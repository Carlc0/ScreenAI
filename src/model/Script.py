class Script:
    def __init__(self, nombre, script, version, requerimientos, descripcion, autor, tipo, fecha_creacion, _id):
        self.nombre = nombre
        self.script = script
        self.version = version
        self.requerimientos = requerimientos
        self.descripcion = descripcion
        self.autor = autor
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self._id = _id

    def fill(self, nombre, script, version, requerimientos, descripcion, autor, tipo, fecha_creacion, _id):
        self.nombre = nombre
        self.script = script
        self.version = version
        self.requerimientos = requerimientos
        self.descripcion = descripcion
        self.autor = autor
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion

    #Setters
    def setId(self, _id):
        self._id = _id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setScript(self, script):
        self.script = script

    def setVersion(self, version):
        self.version = version

    def setRequerimientos(self, requerimientos):
        self.requerimientos = requerimientos     

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setAutor(self, autor):
        self.autor = autor

    def setTipo(self, tipo):
        self.tipo = tipo

    def setFechaCreacion(self, fecha_creacion):
        self.fecha_creacion = fecha_creacion  

    #Getters
    def getAll(self):
        return self

    def getId(self):
        return self._id

    def getNombre(self):
        return self.nombre

    def getScript(self):
        return self.script

    def getVersion(self):
        return self.version

    def getRequerimientos(self):
        return self.requerimientos   

    def getDescripcion(self):
        return self.descripcion

    def getAutor(self):
        return self.autor

    def getTipo(self):
        return self.tipo

    def getFechaCreacion(self):
        return self.fecha_creacion
