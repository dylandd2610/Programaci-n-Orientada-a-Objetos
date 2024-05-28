from claseEquipo import Equipo
import csv
#clase Gestor de equipo
class GestorEquipo:
    __ListaEquipo = list
    def __init__(self):
        self.__ListaEquipo = []
    def agregarEquipo(self, unEquipo):
        self.__ListaEquipo.append(unEquipo)
    def mostrarLista(self):
        print("Lista de equipos: ")
        for equipo in self.__ListaEquipo:
            print(f"[{equipo}]")
    def testEquipos(self): #carga de datos del archivo en el gestor
        archivo = open('equipos2024.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                '''Saltear cabecera'''
                bandera = not bandera
            else:
                IdEquipo = fila[0]
                nombre = fila[1]
                golesFavor = int(fila[2])
                golesContra = int(fila[3])
                diferenciaGoles = int(fila[4])
                puntos = int(fila[5])
                unEquipo = Equipo(IdEquipo, nombre, golesFavor, golesContra, diferenciaGoles, puntos)
                self.agregarEquipo(unEquipo)
        archivo.close()
    def obtenerID(self, equipo):
        band = False
        i = 0
        while band is False and i<len(self.__ListaEquipo):
            if self.__ListaEquipo.getNombre() == equipo:
                IdEquipo = self.__ListaEquipo[i].getId() 
                band = True
            else:
                i += 1
        if band is False:
            return -1
        else:
            return IdEquipo
    def obtenerIndice(self, IdEquipo):
        i = 0
        band = False
        while band is False and i<len(self.__ListaEquipo):
            if self.__ListaEquipo[i].getId() == IdEquipo:
                band == True
            else:
                i += 1
        return i
    def actualizar(self, datos):
        for unEquipo in datos:
            IdLocal = unEquipo[0]
            IdVisitante = unEquipo[1]
            indiceLocal = self.obtenerIndice(IdLocal)
            indiceVisitante = self.obtenerIndice(IdVisitante)
            self.__ListaEquipo[indiceLocal].modificar(unEquipo[2], unEquipo[3])
            self.__ListaEquipo[indiceVisitante].modificar(unEquipo[3], unEquipo[2])
    def getPosiciones(self):
        lista = []
        for unEquipo in self.__ListaEquipo:
            equipos = []
            equipos.append(unEquipo.getId())
            equipos.append(unEquipo.getNombre())
            equipos.append(unEquipo.getGolesFavor())
            equipos.append(unEquipo.getGolesContra())
            equipos.append(unEquipo.getDiferenciaGoles())
            equipos.append(unEquipo.getPuntos())
            lista.append(equipos)
        return lista
    def mostrarPosiciones(self):
        lista = self.getPosiciones()
        for equipo in lista:
            print("ID       nombre      golesF       golesC     difGol       puntos")
            Id = lista[0]
            nombre = lista[1]
            gf = lista[2]
            gc = lista[3]
            dg = lista[4]
            puntos = lista[5]
            print(f"{Id}        {nombre}        {gf}        {gc}        {dg}        {puntos}")
    def ordenar(self):
        self.__ListaEquipo =sorted(self.__ListaEquipo, reverse = True)
    def guardarCSV(self):
        lista = self.getPosiciones()
        archivo = open('archivoPosiciones.csv', mode = 'w', newline = '')
        writer = csv.writer(archivo, delimiter = ';')
        for fila in lista:
            writer.writerow(fila)
        archivo.close()
        print("Se guardaron los datos exitosamente")
    def eliminarEquipo(self, Id):
        i = self.obtenerIndice(Id)
        del self.__ListaEquipo[i]