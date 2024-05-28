from claseEdificio import Edificio
from claseDepartamento import Departamento
import csv
class GestorEdificio:
    __listaEdificios: list
    def __init__(self):
        self.__listaEdificios = []
    def agregarEdificio(self, unEdificio):      #agrega un edificio al gestor
        self.__listaEdificios.append(unEdificio)
    def mostrarEdificioDepa(self):         #muestra lista de edificios y de departamentos
        print("Lista de edificios")
        for edificio in self.__listaEdificios:
            print(f"[{edificio}]")
            edificio.mostrarLista()
    def testEdificios(self):        #agrega edificios y departamentos desde un archivo csv
        archivo = open('EdificioNorte.csv')
        reader = csv.reader(archivo, delimiter = ';')
        unEdificio = None
        for fila in reader:
            if len(fila) == 6:
                Id = int(fila[0])
                nom = fila[1]
                Dir = fila[2]
                nomE = fila[3]
                cantP = int(fila[4])
                cantD = int(fila[5])
                unEdificio = Edificio(Id, nom, Dir, nomE, cantP, cantD)
                self.agregarEdificio(unEdificio)
            elif len(fila) == 8:
                Id = int(fila[1])
                nomApe = fila[2]
                numP = int(fila[3])
                numD = int(fila[4])
                cantH = int(fila[5])
                cantB = int(fila[6])
                sup = float(fila[7])
                unDepa = Departamento(Id, nomApe, numP, numD, cantH, cantB, sup)
                unEdificio.agregarDepa(unDepa)
        archivo.close()
    def mostrarPropietarios(self, nom):     #muestra los propietarios de los departamentos de un edificio
        i = 0
        band = False
        while band is False and i<len(self.__listaEdificios):
            if self.__listaEdificios[i].getNom() == nom:
                print("Nombre y Apellido")
                self.__listaEdificios[i].mostrarNomApe()
                band = True
            else:
                i += 1
        if not band:
            raise TypeError(f"No se encontro el edificio {nom}")
    def mostrarTotalSuper(self, nom):       #muestra la superficie total de un edificio
        i = 0
        band = False
        while band is False and i<len(self.__listaEdificios):
            if self.__listaEdificios[i].getNom() == nom:
                total = self.__listaEdificios[i].calculaSuperficieTotal()
                band = True
            else:
                i += 1
        if not band:
            raise TypeError(f"Error. No se encontro el edificio {nom}")
        print(f"Superficie total del edificio {nom}: {total}")
    def indicarSuperficie(self, nom):       #Muestra la superficie de un departamento y el porcentaje del total que representa
        band = False
        totalP = 0.0
        totalE = 0.0
        for edificio in self.__listaEdificios:
            if edificio.buscarPropietario(nom):
                totalP += edificio.getTotalCubierto(nom)
                totalE += edificio.calculaSuperficieTotal()
                band = True
        assert band is True
        porcentaje = (totalP/totalE)*100
        print(f"Total edificio/s: {totalE}")
        print(f"Superficie cubierta: {round(totalP, 2)}")
        print(f"Porcentaje del total que representa: {round(porcentaje, 2)}%")
    def informaCantDepa(self, numP):        #informa la cantidad de departamentos con 3 habitaciones y mas de 1 banio
        total = 0
        band = False
        for edificio in self.__listaEdificios:
            if edificio.buscarPiso(numP):
                total += edificio.contarCantDepa(numP)
                band = True
        assert band is True
        print(f"Cantidad de departamentos con 3 habitaciones y mas de 1 banio: {total}")