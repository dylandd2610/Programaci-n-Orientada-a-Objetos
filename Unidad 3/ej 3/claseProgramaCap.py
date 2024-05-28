class ProgramaCap:
    __nom: str
    __cod: str
    __dur: int
    __listaMatriculas: list
    def __init__(self, nom, cod, dur):
        self.__nom = nom
        self.__cod = cod
        self.__dur = dur
        self.__listaMatriculas = []
    def __str__(self):
        return "%s %s %s" % (self.__nom, self.__cod, self.__dur)
    def agregarMatricula(self, unaMatricula):
        self.__listaMatriculas.append(unaMatricula)
    def mostrarMatriculas(self):
        print("Listado de matriculas")
        for matricula in self.__listaMatriculas:
            print(f"[{matricula}]")
    def getNom(self):
        return self.__nom
    def getCod(self):
        return self.__cod
    def getDur(self):
        return self.__dur
    def informarMatriculados(self):     #muestra el nombre de todos los empleados matriculados en este programa
        if len(self.__listaMatriculas)>0:
            print(f"Empleados matriculados en el programa {self.getNom()}")
            for matricula in self.__listaMatriculas:
                print(f"{matricula.getNomEmpleado()}")
        else:
            print(f"El programa {self.getNom()} no tiene matriculados")
