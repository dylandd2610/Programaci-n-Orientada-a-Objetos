#clase fechas de futbol
class FechaFutbol:
    __fecha: str
    __IdEquipoLocal: str
    __IdEquipoVisitante: str
    __cantGolesLocal: int
    __cantGolesVisitante: int
    def __init__(self, fecha, IdEquipoL, IdEquipoV, cantGolesL, cantGolesV):
        self.__fecha = fecha
        self.__IdEquipoLocal = IdEquipoL
        self.__IdEquipoVisitante = IdEquipoV
        self.__cantGolesLocal = cantGolesL
        self.__cantGolesVisitante = cantGolesV
    def __str__(self):
        return "%s %s %s %s %s" % (self.__fecha, self.__IdEquipoLocal, self.__IdEquipoVisitante, self.__cantGolesLocal, self.__cantGolesVisitante)
    def getFecha(self):
        return self.__fecha
    def getIdEquipoLocal(self):
        return self.__IdEquipoLocal
    def getIdEquipoVisitante(self):
        return self.__IdEquipoVisitante
    def getCantGolesL(self):
        return self.__cantGolesLocal
    def getCantGolesV(self):
        return self.__cantGolesVisitante