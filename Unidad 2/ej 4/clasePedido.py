class Pedido: #clase pedido
    __patente: str
    __idPedido: int
    __comidas: str
    __tiempoEst: int
    __tiempoReal: int
    __precio: float
    def __init__(self, patente, idPedido, comidas, tiempoEst, tiempoReal, precio):
        self.__patente = patente
        self.__idPedido = idPedido
        self.__comidas = comidas
        self.__tiempoEst = tiempoEst
        self.__tiempoReal = tiempoReal
        self.__precio = precio
    def __str__(self):
        return "%s %s %s %s %s %s" % (self.__patente, self.__idPedido, self.__comidas, self.__tiempoEst, self.__tiempoReal, self.__precio)
    def getPatente(self):
        return self.__patente
    def getId(self):
        return self.__idPedido
    def getComidas(self):
        return self.__comidas
    def getTiempoEst(self):
        return self.__tiempoEst
    def getTiempoReal(self):
        return int(self.__tiempoReal)
    def getPrecio(self):
        return float(self.__precio)
    def setTiempoReal(self, tiempoR):
        self.__tiempoReal = tiempoR
    def __lt__(self, otro):
        return self.__patente < otro.getPatente()