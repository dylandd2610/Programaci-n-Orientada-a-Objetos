class Matricula:
    __fecha: str
    __empleado: object
    __programa: object
    def __init__(self, fecha, empleado, programa):
        self.__fecha = fecha
        self.__empleado = empleado
        self.__programa = programa
    def __str__(self):
        return "%s %s %s" % (self.__fecha, self.__empleado, self.__programa)
    def getFecha(self):
        return self.__fecha
    def getEmpleado(self):
        return self.__empleado
    def getMatricula(self):
        return self.__programa
    def getDurPrograma(self):   #retorna de la duracion de su instancia de programa
        return self.__programa.getDur()
    def getNomPrograma(self):   #retorna el nombre de su instancia de programa
        return self.__programa.getNom()
    def getNomEmpleado(self):   #retorna el nombre y apellido de su instancia de empleado
        return self.__empleado.getNomApe()
    def getIdEmpleado(self):    #retorna el Id de su instancia de empleado
        return self.__empleado.getId()