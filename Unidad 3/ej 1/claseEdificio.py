class Edificio:
    __Id: int
    __nom: str
    __Dir: str
    __nomE: str
    __cantP: int
    __cantD: int
    __listaDepa: list
    def __init__(self, Id, nom, Dir, nomE, cantP, cantD):
        self.__Id = Id
        self.__nom = nom
        self.__Dir = Dir
        self.__nomE = nomE
        self.__cantP = cantP
        self.__cantD = cantD
        self.__listaDepa = []
    def __str__(self):
        return "%s %s %s %s %s %s" % (self.__Id, self.__nom, self.__Dir, self.__nomE, self.__cantP, self.__cantD)
    def mostrarLista(self):     #muestra lista de departamentos
        for depa in self.__listaDepa:
            print(f"    [{depa}]")
    def agregarDepa(self, unDepa):      #agrega un departamento a la lista
        self.__listaDepa.append(unDepa)
    def getId(self):
        return self.__Id
    def getNom(self):
        return self.__nom
    def getDir(self):
        return self.__Dir
    def getNomE(self):
        return self.__nomE
    def getCantP(self):
        return self.__cantP
    def getCantD(self):
        return self.__cantD
    def mostrarNomApe(self):        #muestra nombre y apellido de todos los propietarios de este edificio
        for depa in self.__listaDepa:
            print(f"{depa.getNomApe()}")
    def calculaSuperficieTotal(self):       #suma la superficie de todos los departamentos
        total = 0.0
        for depa in self.__listaDepa:
            total += depa.getSup()
        return total
    def buscarPropietario(self, nomApe):        #busca un propietario por su nombre y retorna si existe
        i = 0
        band = False
        while band is False and i<len(self.__listaDepa):
            if self.__listaDepa[i].getNomApe() == nomApe:
                band = True
            else:
                i += 1
        return band
    def getTotalCubierto(self, nomApe):     #cuenta y retorna es total de la superficie de todos los departamentos de un propietario
        total = 0.0
        for depa in self.__listaDepa:
            if depa.getNomApe() == nomApe:
                total += depa.getSup()
        return total
    def buscarPiso(self, numP):         #Busca si existe el numero de piso solicitado
        band = False
        i = 0
        while band is False and i<len(self.__listaDepa):
            if self.__listaDepa[i].getNumP() == numP:
                band = True
            else:
                i += 1
        return band
    def contarCantDepa(self, numP):         #cuenta cantidad de departamentos con 3 habitaciones y mas de un banio para un piso
        cant = 0
        for depa in self.__listaDepa:
            if depa.getNumP() == numP:
                if depa.getCantH() == 3 and depa.getCantB() > 1:
                    cant += 1
        return cant