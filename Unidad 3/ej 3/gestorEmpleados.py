from claseEmpleado import Empleado
import csv
class GestorEmpleados:
    __listaEmpleados: list
    def __init__(self):
        self.__listaEmpleados = []
    def agregarEmpleado(self, unEmpleado):      #agrega un empleado al gestor
        self.__listaEmpleados.append(unEmpleado)
    def mostrarEmpleados(self):         #muestra un listado de los empleados
        print("Listado de empleados")
        for empleado in self.__listaEmpleados:
            print(f"[{empleado}]")
    def testEmpleados(self):        #agrega datos de un archivo csv al gestor
        archivo = open('archivoEmpleados.csv')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                """saltear cabecera"""
                band = not band
            else:
                nomApe = fila[0]
                Id = int(fila[1])
                puesto = fila[2]
                unEmpleado = Empleado(nomApe, Id, puesto)
                self.agregarEmpleado(unEmpleado)
        archivo.close()
    def buscarEmpleado(self, Id):       #busca un empleado segun si Id y lo retorna
        i = 0
        band = False
        while not band and i<len(self.__listaEmpleados):
            if self.__listaEmpleados[i].getId() == Id:
                unEmpleado = self.__listaEmpleados[i]
                band = True
            else:
                i += 1
        if band:
            return unEmpleado
        else:
            return -1
    def informarDuracionProgramas(self, Id):    #informa nombre y duracion de cada programa en el que se matriculo un empleado
        i = 0
        band = False
        while not band and i<len(self.__listaEmpleados):
            if self.__listaEmpleados[i].getId() == Id:
                print("Programa de Capacitacion         Duracion")
                self.__listaEmpleados[i].getProgramaDur()
                band = True
            else:
                i += 1
        assert band is True
    def informarNoMatriculados(self, gm):       #muestra empleados no matriculados
        print("Empleados no matriculados")
        print("Nombre y Apellido         Id          Puesto")
        for empleado in self.__listaEmpleados:
            if gm.buscarEmpleado(empleado.getId()) == False:
                print(f"{empleado.getNomApe()}            {empleado.getId()}          {empleado.getPuesto()}")