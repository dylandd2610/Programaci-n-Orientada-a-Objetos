from claseCuenta import Cuenta
import numpy as np
import csv
class GestorCuentas:
    __cantidad: int
    __dimension: int
    __incremento: int
    __ListaCuentas: np.ndarray
    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 5
        self.__ListaCuentas = np.empty(self.__dimension, dtype = Cuenta)
    def agregarCuenta(self, unaCuenta):
        if self.__cantidad == self.__dimension:
            print("Se solicito espacio")
            self.__dimension += self.__incremento
            self.__ListaCuentas.resize(self.__dimension)
        self.__ListaCuentas[self.__cantidad] = unaCuenta
        self.__cantidad += 1
    def mostrarLista(self):
        for fila in self.__ListaCuentas:
            print(fila)
    def testCuentas(self): #carga de datos del archivo en el gestor
        archivo = open('cuentasBilletera.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band:
                '''saltar cabecera'''
                band = not band
            else:
                apellido = fila[0]
                nombre = fila[1]
                DNI = int(fila[2])
                telefono = int(fila[3])
                saldo = float(fila[4])
                CVU = int(fila[5])
                unaCuenta = Cuenta(apellido, nombre, DNI, telefono, saldo, CVU)
                self.agregarCuenta(unaCuenta)
        self.__ListaCuentas.resize(self.__cantidad)
        archivo.close()
    def buscarIndice(self, xdni): #busca el indice de una cuenta por medio del DNI
        band = False
        i = 0
        while band != True and i < len(self.__ListaCuentas):
            if self.__ListaCuentas[i].getDNI() == xdni:
                band = True
            else:
                i += 1
        if band == True:
            return i
        else:
            return -1
    def informarDatosActualizados(self, listaT, xdni): #actualiza el saldo de la cuenta luego de las transacciones y muestra los datos
        i = self.buscarIndice(xdni)
        if i == -1:
            print(f"No se encontro la cuenta para el dni: {xdni}")
        else:
            cvu = self.__ListaCuentas[i].getCVU()
            for transaccion in listaT:
                if cvu == transaccion[0]:
                    self.__ListaCuentas[i].actualizarSaldo(transaccion[1], transaccion[2])
            ape = self.__ListaCuentas[i].getApellido()
            nom = self.__ListaCuentas[i].getNombre()
            saldo = self.__ListaCuentas[i].getSaldo()
            print("Apellido       Nombre         CVU        Saldo")
            print(f"{ape}       {nom}       {cvu}           {saldo}")
    def modifiVarClase(self, nuevaVar): #modifica la variable de clase
        self.__ListaCuentas[0].modificar(nuevaVar)
    def actualizarSaldo(self):
        porcentaje = self.__ListaCuentas[0].getIncrementoDiario()
        for i in range(self.__cantidad):
            self.__ListaCuentas[i].incrementarSaldo(porcentaje)
    def getIndiceCVU(self, CVU): #obtener indice por medio de cvu
        band = False
        i = 0
        while band is False and i<len(self.__ListaCuentas):
            if self.__ListaCuentas[i].getCVU() == CVU:
                band = True
            else:
                i += 1
        if band == True:
            return i
        else:
            return -1
    def procesarTransacciones(self, CVU, listaT):
        i = self.getIndiceCVU(CVU)
        if i == -1:
            print(f"No se encontro la cuenta del CVU: {CVU}")
        else:
            print(f"Saldo inicial: {self.__ListaCuentas[i].getSaldo()}")
            CVU = self.__ListaCuentas[i].getCVU()
            for transaccion in listaT:
                if CVU == transaccion[0]:
                    self.__ListaCuentas[i].actualizarSaldo(transaccion[1], transaccion[2])
            print(f"Nuevo saldo: {self.__ListaCuentas[i].getSaldo()}")
    def actualizarTodas(self, listaT): #actualizar el saldo de todas las cuentas
        for cuenta in self.__ListaCuentas:
            for transaccion in listaT:
                if cuenta.getCVU() == transaccion[0]:
                    cuenta.actualizarSaldo(transaccion[1], transaccion[2])
    def getListaCuentas(self):
        lista = []
        for cuenta in self.__ListaCuentas:
            otraLista = []
            otraLista.append(cuenta.getApellido())
            otraLista.append(cuenta.getNombre())
            otraLista.append(cuenta.getDNI())
            otraLista.append(cuenta.getTelefono())
            otraLista.append(cuenta.getSaldo())
            otraLista.append(cuenta.getCVU())
            lista.append(otraLista)
        return lista
    def almacenarCSV(self): #guardar la lista del gestor en un archivo
        listaCuentas = self.getListaCuentas()
        archivo = open('archivoCSV.csv', mode = 'w', newline = '')
        writer = csv.writer(archivo, delimiter = ';')
        for fila in listaCuentas:
            writer.writerow(fila)
        archivo.close()
        print("Se almacenaron los datos correctamente")
    def getIndice(self, cvu): #obtener el indice de una cuenta a traves del cvu
        i = 0
        band = False
        while band is False and i<len(self.__ListaCuentas):
            if self.__ListaCuentas[i].getCVU() == cvu:
                band = True
            else:
                i += 1
        if band == True:
            return i
        else:
            return -1
    def eliminarCuenta(self, cvu): #eliminar una cuenta
        i = self.getIndice(cvu)
        if i != -1:
            self.__ListaCuentas = np.delete(self.__ListaCuentas, i)
            print("Se elimino la cuenta correctamente")
        else:
            print("No se encontro la cuentan con ese CVU")