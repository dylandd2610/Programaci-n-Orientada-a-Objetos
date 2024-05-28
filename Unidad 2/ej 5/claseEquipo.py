#clase equipo
class Equipo:
    __IdEquipo: str
    __nombre: str
    __golesFavor: int
    __golesContra: int
    __diferenciaGoles: int
    __puntos: int
    def __init__(self, idEquipo, nombre, golesFavor, golesContra, diferenciaGoles, puntos):
        self.__IdEquipo = idEquipo
        self.__nombre = nombre
        self.__golesFavor = golesFavor
        self.__golesContra = golesContra
        self.__diferenciaGoles = diferenciaGoles
        self.__puntos = puntos
    def __str__(self):
        return "%s %s %s %s %s %s" % (self.__IdEquipo, self.__nombre, self.__golesFavor, self.__golesContra, self.__diferenciaGoles, self.__puntos)
    def getId(self):
        return self.__IdEquipo
    def getNombre(self):
        return self.__nombre
    def getGolesFavor(self):
        return self.__golesFavor
    def getGolesContra(self):
        return self.__golesContra
    def getDiferenciaGoles(self):
        return self.__diferenciaGoles
    def getPuntos(self):
        return self.__puntos
    def modificar(self, gf, gc):
        dg = gf = gc
        self.__golesFavor += gf
        self.__golesContra += gc
        self.__diferenciaGoles += dg
        if dg == 0:
            self.__puntos += 1
        elif dg > 0:
            self.__puntos += 3
    def __gt__(self, otro):
        if self.__puntos == otro.getPuntos():
            if self.__diferenciaGoles == otro.getDiferenciaGoles():
                return self.__golesFavor > otro.getGolesFavor()
            else:
                return self.__diferenciaGoles > otro.getDiferenciaGoles()
        else:
            return self.__puntos > otro.getPuntos()
    def __del__(self):
        print("Se elimino correctamente el equipo:", self.__nombre)