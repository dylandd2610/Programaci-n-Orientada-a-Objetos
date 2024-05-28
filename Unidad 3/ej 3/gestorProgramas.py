from claseProgramaCap import ProgramaCap
import csv
class GestorProgramas:
    __listaProgramas: list
    def __init__(self):
        self.__listaProgramas = []
    def agregarPrograma(self, unPrograma):      #agrega un programa al gestor
        self.__listaProgramas.append(unPrograma)
    def mostrarProgramas(self):         #muestra un listado de los programas
        print("Listado de Programas")
        for programa in self.__listaProgramas:
            print(f"[{programa}]")
    def testProgramas(self):        #carga datos de un archivo csv al gestor
        archivo = open('archivoProgramas.csv')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                nom = fila[0]
                cod = fila[1]
                dur = int(fila[2])
                unPrograma = ProgramaCap(nom, cod, dur)
                self.agregarPrograma(unPrograma)
        archivo.close()
    def buscarPrograma(self, cod):      #busca un programa segun su codigo y lo retorna
        i = 0
        band = False
        while not band and i<len(self.__listaProgramas):
            if self.__listaProgramas[i].getCod() == cod:
                unPrograma = self.__listaProgramas[i]
                band = True
            else:
                i += 1
        if band:
            return unPrograma
        else:
            return -1
    def informarEmpleadosMat(self, nom):    #muestra los empleados matriculados en un programa
        i = 0
        band = False
        while not band and i<len(self.__listaProgramas):
            if self.__listaProgramas[i].getNom() == nom:
                self.__listaProgramas[i].informarMatriculados()
                band = True
            else:
                i += 1
        assert band is True