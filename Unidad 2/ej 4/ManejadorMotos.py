import csv
from claseMoto import Moto
class ManejadorMotos:
    def __init__(self):
        self.__ListaMotos = []
    def agregarMoto(self, unaMoto):
        self.__ListaMotos.append(unaMoto)
    def mostrarLista(self):
        for moto in self.__ListaMotos:
            print(f"[{moto}]")
    def testMoto(self):
        archivo = open('datosMotos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                patente = fila[0]
                marca = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                kilometraje = int(fila[4])
                unaMoto = Moto(patente, marca, nombre, apellido, kilometraje)
                self.agregarMoto(unaMoto)
        archivo.close()
    def getListaPatentes(self):
        lista = []
        for i in self.__ListaMotos:
            lista.append(i.getPatente())
        return lista
    def getDatos(self, patente):
        bandera = False
        lista = []
        i = 0
        while bandera is False and i<len(self.__ListaMotos):
            if self.__ListaMotos[i].getPatente() == patente:
                lista.append(self.__ListaMotos[i].getNombre())
                lista.append(self.__ListaMotos[i].getApellido())
                lista.append(self.__ListaMotos[i].getMarca())
                lista.append(self.__ListaMotos[i].getKilometraje())
                bandera = not bandera
            else:
                i += 1
        if bandera is False:
            return -1
        else: 
            return lista
    def getConductor(self):
        lista = []
        for i in self.__ListaMotos:
            lista.append(i.getNombre())
        return lista