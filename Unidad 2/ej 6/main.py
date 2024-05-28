from GestorCuentas import GestorCuentas
from GestorTransacciones import GestorTransacciones
import numpy
import csv

def menu():
    opcion = input("""Seleccione alguna de las siguienes opciones:
1_Leer por teclado el DNI de un cliente e informar los datos del cliente
2_Leer por teclado el nuevo porcentaje anual del rendimiento, modificarlo para la clase Cuenta
3_Actualizar el saldo, incrementándolo para todos los clientes, en función del porcentaje anual de rendimiento
4_Leer por teclado un número de CVU, informar el saldo inicial, procesar todas las transacciones, y obtener el nuevo sado actualizado
5_Almacenar los datos actualizados de las Cuentas en un archivo .csv
6_Eliminar una cuenta del gestor
7_Mostrar cuentas 
8_Mostrar transacciones
0_salir
--> """)
    return opcion

if __name__=='__main__':
    #crear, inicializar y mostrar cuentas
    gc = GestorCuentas()
    gc.testCuentas()
    #crear, inicializar y mostrar transacciones
    gt = GestorTransacciones()
    gt.testTransacciones()
    opcion = menu()
    while opcion != "0":
        if opcion == "1":
            listaT = gt.getListaTransacciones()
            dni = int(input("Ingrese el DNI de la cuenta que busca: "))
            gc.informarDatosActualizados(listaT, dni)
        elif opcion == "2":
            nuevaVar = float(input("Ingrese un nuevo porcentaje anual: "))
            gc.modifiVarClase(nuevaVar)
        elif opcion == "3":
            gc.actualizarSaldo()
        elif opcion == "4":
            listaTran =  gt.getListaTransacciones()
            cvu = int(input("Ingrese un cvu a buscar para mostrar actualizar saldo:"))
            gc.procesarTransacciones(cvu, listaTran)
        elif opcion == "5":
            listaT2 = gt.getListaTransacciones()
            gc.actualizarTodas(listaT2)
            gc.almacenarCSV()
        elif opcion == "6":
            cvuEliminar = int(input("Ingrese el CVU de la cuenta a eliminar: "))
            gc.eliminarCuenta(cvuEliminar)
        elif opcion == "7":
            gc.mostrarLista()
        elif opcion == "8":
            gt.mostrarLista()
        else:
            print("Opcion invalida")
        opcion = menu()