class MaterialRefractario:
    __mat: int
    __caract: str
    __cantutillizada: float
    __costo: float
    def __init__(self, mat, caract, cantu, costo):
        self.__mat = mat
        self.__caract = caract
        self.__cantutillizada = cantu
        self.__costo = costo
    def __str__(self):
        return "%s %s %s %s" % (self.__mat, self.__caract, self.__cantutillizada, self.__costo)
    def getMaterial(self):
        return self.__mat
    def getCaract(self):
        return self.__caract
    def getCantu(self):
        return self.__cantutillizada
    def getCosto(self):
        return self.__costo