from claseMaterial import MaterialRefractario
import csv
class GestorMaterial:
    __listaMateriales: list
    def __init__(self):
        self.__listaMateriales = []
    def agregarMaterial(self, unMaterial):   #agrega un material a la lista
        self.__listaMateriales.append(unMaterial)
    def mostrarMateriales(self):         #muestra la lista de materiales
        print("Listado de materiales")
        for material in self.__listaMateriales:
            print(f"[{material}]")
    def testMateriales(self):       #agrega materiales de un archivo csv al gestor
        archivo = open('materiales.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                '''saltear cabecera'''
                band = not band
            else:
                mat = int(fila[0])
                caract = fila[1]
                cantu = float (fila[2])
                costo = float(fila[3])
                unMaterial = MaterialRefractario(mat, caract, cantu, costo)
                self.agregarMaterial(unMaterial)
        archivo.close()
    def buscarMaterial(self, mat):      #busca un material y lo retorna
        i = 0
        band = False
        while not band and i<len(self.__listaMateriales):
            if self.__listaMateriales[i].getMaterial() == mat:
                unMaterial = self.__listaMateriales[i]
                band = True
            else:
                i += 1
        if band:
            return unMaterial
        else:
            return -1