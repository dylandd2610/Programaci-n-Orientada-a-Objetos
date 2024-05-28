from claseTransaccion import Transaccion
import csv
class GestorTransacciones:
    __ListaTransacciones: list
    def __init__(self):
        self.__ListaTransacciones = []
    def agregarTransaccion(self, unaTransaccion):
        self.__ListaTransacciones.append(unaTransaccion)
    def mostrarLista(self):
        for fila in self.__ListaTransacciones:
            print(fila)
    def testTransacciones(self): #carga de datos del archivo en el gestor
        archivo = open('transaccionesBilletera.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                '''saltar cabecera'''
                band = not band
            else:
                CVU = int(fila[0])
                numT = int(fila[1])
                imp = float(fila[2])
                tipoT = fila[3]
                unaTransaccion = Transaccion(CVU, numT, imp, tipoT)
                self.agregarTransaccion(unaTransaccion)
        archivo.close()
    def getListaTransacciones(self): #genera lista de transacciones y la retorna
        listaT = []
        for fila in self.__ListaTransacciones:
            T = []
            T.append(fila.getCVU())
            T.append(fila.getImporte())
            T.append(fila.getTipoT())
            listaT.append(T)
        return listaT