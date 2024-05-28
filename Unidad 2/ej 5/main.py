from GestorEquipo import GestorEquipo
from GestorFechas import GestorFechas
import csv

if __name__ == '__main__':
    opcion = input(""""Seleccione una de las siguientes opciones:
                   1_Leer los datos de los equipos de un archivo csv y almacenarlos en un gestor
                   2_Leer los datos de las fechas de futbol de un archivo csv y almacenarlos en un gestor
                   3_Leer el nombre de un equipo y obtener un listado
                   4_Actualizar la tabla de todos los equipos, con los resultados de las fechas disputadas
                   5_Ordenar la tabla de posiciones de mayor a menor
                   6_Almacenar la tabla de posiciones en un archivo csv
                   7_Eliminar un equipo
                   0_salir
                   """)
    while opcion != 0:
        if opcion == "1":
            ge = GestorEquipo()
            ge.testEquipos()
            ge.mostrarLista()
        elif opcion == "2":
            gf = GestorFechas()
            gf.testFechas()
            gf.mostrarLista()
        elif opcion == "3":
            nombre = input("Ingrese un nombre de un equipo para buscar si ID: ")
            ID = ge.obtenerID(nombre)
            if ID != -1:
                gf.generarListado(ID, nombre)
            else:
                print("El equipo no existe")
        elif opcion == "4":
            fechas = gf.obtenerDatosFechas()
            ge.actualizar(fechas)
            ge.mostrarPosiciones()
        elif opcion == "5":
            ge.ordenar()
            ge.mostrarPosiciones()
        elif opcion == "6":
            ge.guardarCSV()
        elif opcion == "7":
            IdEquipo = int(input("Ingresa Id de equipo a eliminar: "))
            ge.eliminarEquipo(IdEquipo)
        opcion = input(""""Seleccione una de las siguientes opciones:
                   1_Leer los datos de los equipos de un archivo csv y almacenarlos en un gestor
                   2_Leer los datos de las fechas de futbol de un archivo csv y almacenarlos en un gestor
                   3_Leer el nombre de un equipo y obtener un listado
                   4_Actualizar la tabla de todos los equipos, con los resultados de las fechas disputadas
                   5_Ordenar la tabla de posiciones de mayor a menor
                   6_Almacenar la tabla de posiciones en un archivo csv
                   7_Eliminar un equipo
                   0_salir
                   """)