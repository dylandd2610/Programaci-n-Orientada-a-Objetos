class Transaccion:
    __CVU: int
    __numTransaccion: int
    __importe: float
    __tipoTransaccion: str
    def __init__(self, CVU, numTransaccion, importe, tipoTransaccion):
        self.__CVU = CVU
        self.__numTransaccion = numTransaccion
        self.__importe = importe
        self.__tipoTransaccion = tipoTransaccion
    def __str__(self):
        return "[%s %s %s %s]" % (self.__CVU, self.__numTransaccion, self.__importe, self.__tipoTransaccion)
    def getCVU(self):
        return self.__CVU
    def getNumT(self):
        return self.__numTransaccion
    def getImporte(self):
        return self.__importe
    def getTipoT(self):
        return self.__tipoTransaccion
    