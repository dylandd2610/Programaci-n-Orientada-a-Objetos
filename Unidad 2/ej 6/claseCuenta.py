class Cuenta:
    __apellido: str
    __nombre: str
    __DNI: int
    __telefono: int
    __saldo: float
    __CVU: int
    porAnual = 68.0
    def __init__(self, apellido, nombre, DNI, telefono, saldo, CVU):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__DNI = DNI
        self.__telefono = telefono
        self.__saldo = saldo
        self.__CVU = CVU
    def __str__(self):
        return "[%s %s %s %s %s %s %s]" % (self.__apellido, self.__nombre, self.__DNI, self.__telefono, self.__saldo, self.__CVU, Cuenta.porAnual)
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getDNI(self):
        return self.__DNI
    def getTelefono(self):
        return self.__telefono
    def getSaldo(self):
        return self.__saldo
    def getCVU(self):
        return self.__CVU
    def actualizarSaldo(self, imp, tipo): #modifica el saldo 
        if tipo == "D":
            self.__saldo -= imp
        elif tipo == "C":
            self.__saldo += imp
    @classmethod
    def modificar(cls, nuevaVar): #modifica la variable de clase porcentaje
        cls.porAnual = nuevaVar
    @classmethod
    def getIncrementoDiario(cls):
        porInicial = round(float(Cuenta.porAnual/365), 2)
        return porInicial
    def incrementarSaldo(self, porInicial): #incrementar saldo segun el porcentaje diario
        self.__saldo += (self.__saldo * porInicial)/100
        self.__saldo = round(self.__saldo, 2)