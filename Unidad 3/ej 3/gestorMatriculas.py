from claseMatricula import Matricula
import csv
class GestorMatriculas:
    __listaMatriculas: list
    def __init__(self):
        self.__listaMatriculas = []
    def agregarMatricula(self, unaMatricula):         #agrega una matricula al gestor
        self.__listaMatriculas.append(unaMatricula)
    def mostrarMatriculas(self):
        print("Listado de matriculas")          #muestra un listado de las matriculas
        for matricula in self.__listaMatriculas:
            print(f"[{matricula}]")
    def testMatriculas(self, ge, gp):       #carga matriculas segun datos de un archivo csv
        archivo = open('archivoMatriculas.csv')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                unEmpleado = ge.buscarEmpleado(int(fila[1]))
                unPrograma = gp.buscarPrograma(fila[2])
                if unEmpleado != -1 and unPrograma != -1:
                    fecha = fila[0]
                    unaMatricula = Matricula(fecha, unEmpleado, unPrograma)
                    unEmpleado.agregarMatricula(unaMatricula)
                    unPrograma.agregarMatricula(unaMatricula)
                    self.agregarMatricula(unaMatricula)
                else:
                    print(f"Empleado de Id {int(fila[1])} y/o Programa de codigo {fila[2]} inexistentes")
        archivo.close()
    def buscarEmpleado(self, Id):       #busca un empleado y retorna si lo encontro o no
        i = 0
        band = False
        while not band and i<len(self.__listaMatriculas):
            if self.__listaMatriculas[i].getIdEmpleado() == Id:
                band = True
            else:
                i += 1
        return band    