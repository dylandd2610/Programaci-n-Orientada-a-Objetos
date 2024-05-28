class Empleado:
    __nomApe: str
    __Id: int
    __puesto: str
    __listaMatriculas: list
    def __init__(self, nomApe, Id, puesto):
        self.__nomApe = nomApe
        self.__Id = Id
        self.__puesto = puesto
        self.__listaMatriculas = []
    def __str__(self):
        return "%s %s %s" % (self.__nomApe, self.__Id, self.__puesto)
    def agregarMatricula(self, unaMatricula):
        self.__listaMatriculas.append(unaMatricula)
    def mostrarMatriculas(self):
        print("Listado de Matriculas")
        for matricula in self.__listaMatriculas:
            print(f"[{matricula}]")
    def getNomApe(self):
        return self.__nomApe
    def getId(self):
        return self.__Id
    def getPuesto(self):
        return self.__puesto
    def getProgramaDur(self):      #muestra nombre y duracion de cada programa en el que se matriculo
        if len(self.__listaMatriculas)>0:
            for matricula in self.__listaMatriculas:
                print(f"{matricula.getNomPrograma()}                  {matricula.getDurPrograma()}")
        else:
            print(f"El empleado de Id {self.getId()} no se matriculo en ningun programa")