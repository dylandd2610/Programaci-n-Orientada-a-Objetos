class Moto: #clase moto
    __patente: str
    __marca: str
    __nombre: str
    __apellido: str
    __kilometraje: int
    def __init__(self, patente, marca, nombre, apellido, kilometraje):
        self.__patente = patente
        self.__marca = marca
        self.__nombre = nombre
        self.__apellido = apellido
        self.__kilometraje = kilometraje
    def __str__(self):
        return "%s %s %s %s %s" % (self.__patente, self.__marca, self.__nombre, self.__apellido, self.__kilometraje)
    def getPatente(self):
        return self.__patente
    def getMarca(self):
        return self.__marca
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getKilometraje(self):
        return self.__kilometraje