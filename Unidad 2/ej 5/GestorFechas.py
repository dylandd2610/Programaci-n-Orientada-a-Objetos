from claseFechas import FechaFutbol
import csv
class GestorFechas:
    __ListaFechas: list
    def __init__(self):
        self.__ListaFechas = []
    def agregarFecha(self, unaFecha):
        self.__ListaFechas.append(unaFecha)
    def mostrarLista(self):
        print("Lista de Fechas: ")
        for fecha in self.__ListaFechas:
            print(f"[{fecha}]")
    def testFechas(self): #carga de datos del archivo al gestor
        archivo = open('fechasFutbol.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                '''Saltear cabecera'''
                bandera = not bandera
            else:
                fecha = fila[0]
                IdEquipoL = fila[1]
                IdEquipoV = fila[2]
                cantGolesL = int(fila[3])
                cantGolesV = int(fila[4])
                unaFecha = FechaFutbol(fecha, IdEquipoL, IdEquipoV, cantGolesL, cantGolesV)
                self.agregarFecha(unaFecha)
        archivo.close()
    def generarListado(self, idEquipo, nomEquipo):
        gfTotal = 0
        gcTotal = 0
        difTotal = 0
        puntosTotal = 0
        print(f"""Equipo: {nomEquipo}
            Fecha       Goles a Favor       Goles en Contra        Diferencia de Goles       Puntos""")
        for fecha in self.__ListaFechas:
            fecha = fecha.getFecha()
            IdEquipoLocal = fecha.getIdEquipoLocal()
            IdEquipoVisitante = fecha.getIdEquipoVisitante()
            jugo = False
            if IdEquipoLocal == idEquipo:
                gf = fecha.getCantGolesL()
                gc = fecha.getCantGolesV()
                jugo = True
            elif IdEquipoVisitante == idEquipo:
                gf = fecha.getCantGolesV()
                gc = fecha.getCantGolesL()
                jugo = True
            else:
                gf = 0
                gc = 0
            dg = gf - gc
            if gf == gc:
                puntos = 1
            elif gf > gc:
                puntos = 3
            else:
                puntos = 0   
            if jugo is True:
                print(f"""{fecha}       {gf}        {gc}        {dg}        {puntos}""")
                gfTotal += gf
                gcTotal += gc
                difTotal += dg
                puntosTotal += puntos
        print(f"""Totales:    {gfTotal}      {gcTotal}       {difTotal}         {puntosTotal}""")
    def obtenerDatosFechas(self):
        lista = []
        for unaFecha in self.__ListaFechas:
            fechaDatos = []
            fechaDatos.append(unaFecha.getIdEquipoLocal())
            fechaDatos.append(unaFecha.getIdEquipoVisitante())
            fechaDatos.append(unaFecha.getCantGolesL())
            fechaDatos.append(unaFecha.getCantGolesV())
            lista.append(fechaDatos)
        return lista