class Departamento:
    __Id: int
    __nomApe: str
    __numP: int
    __numD: int
    __cantH: int
    __cantB: int
    __sup: float
    def __init__(self, Id, nomApe, numP, numD, cantH, cantB, sup):
        self.__Id = Id
        self.__nomApe = nomApe
        self.__numP = numP
        self.__numD = numD
        self.__cantH = cantH
        self.__cantB = cantB
        self.__sup = sup
    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.__Id, self.__nomApe, self.__numP, self.__numD, self.__cantH, self.__cantB, self.__sup)
    def getId(self):
        return self.__Id
    def getNomApe(self):
        return self.__nomApe
    def getNumP(self):
        return self.__numP
    def getNumD(self):
        return self.__numD
    def getCantH(self):
        return self.__cantH
    def getCantB(self):
        return self.__cantB
    def getSup(self):
        return self.__sup