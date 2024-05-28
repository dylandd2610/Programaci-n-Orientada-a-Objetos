from claseLadrillo import Ladrillo
import csv
class GestorLadrillo:
    __listaLadrillos = list
    def __init__(self):
        self.__listaLadrillos = []
    def agregarLadrillo(self, unLadrillo):      #agrega un ladrillo a la lista
        self.__listaLadrillos.append(unLadrillo)
    def mostrarLadrillos(self):      #muestra la lista de ladrillos
        print("Listado de ladrillos")
        for ladrillo in self.__listaLadrillos:
            print(f"[{ladrillo}]")
            ladrillo.mostrarListaMat()
    def testLadrillos(self, gm):        #carga ladrillos de un archivo al gestor
        archivo = open('ladrillos.csv')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                '''saltear cabecera'''
                band = not band
            else:
                cant = int(fila[0])
                Id = int(fila[1])
                kg = float(fila[2])
                costo = float(fila[3])
                unLadrillo = Ladrillo(cant, Id, kg, costo)
                print(f"Carga de materiales para el ladrillo de id {Id}")
                mat = int(input("Ingrese un numero de material. 0 para dejar de agregar materiales: "))
                while mat != 0:
                    unMaterial = gm.buscarMaterial(mat)
                    if unMaterial != -1:
                        unLadrillo.agregarMaterial(unMaterial)
                    else:
                        print("Error. El material no existe")
                    mat = int(input("Ingrese un numero de material. 0 para dejar de agregar materiales: "))
                self.agregarLadrillo(unLadrillo)
        archivo.close()
    def InformarDatosLadrillo(self, Id):    #muestra costo y caracteristicas de los materiales de un ladrillo
        i = 0
        band = False
        while not band and i<len(self.__listaLadrillos):
            if self.__listaLadrillos[i].getId() == Id:
                self.__listaLadrillos[i].informarDatos()
                band = True
            else:
                i += 1
        assert band is True
    def mostrarCostoTotal(self):        #muestra el costo total de cada ladrillo
        print("Costo total de los ladrillos")
        print("Id       Costo Total")
        for ladrillo in self.__listaLadrillos:
            print(f"{ladrillo.getId()}           {ladrillo.calcularTotal()}")
    def informarMaterial(self):         #informa Id, materiales y costo adicional de un ladrillo
        print("Ladrillos fabricados")
        print("Id        Material         Costo Asociado")
        for ladrillo in self.__listaLadrillos:
            Id = ladrillo.getId()
            mat = ladrillo.contarMat()
            if mat != "":
                costoAd = ladrillo.costoAdicional()
                print(f"{Id}            {mat}             {costoAd}")
            else:
                print(f"{Id}              -                   -")   