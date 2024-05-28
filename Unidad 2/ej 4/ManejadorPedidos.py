import csv
from clasePedido import Pedido
class ManejadorPedidos:
    def __init__(self):
        self.__ListaPedidos = []
    def agregarPedido(self, unPedido):
        self.__ListaPedidos.append(unPedido)
    def mostrarLista(self):
        for pedido in self.__ListaPedidos:
            print(f"[{pedido}]")
    def testPedidos(self):
        archivo = open('datosPedido.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                patente = fila[0]
                idPedido = fila[1]
                comidas = fila[2]
                tiempoEst = fila[3]
                tiempoReal = fila[4]
                precio = float(fila[5])
                unPedido = Pedido(patente, idPedido, comidas, tiempoEst, tiempoReal, precio)
                self.agregarPedido(unPedido)
        archivo.close()
    def ordenar(self):
        #print(self.__ListaPedidos)
        self.__ListaPedidos = sorted(self.__ListaPedidos)
    def cargaPedido(self, patentes):
        unaPatente = input("Ingrese una patente para buscar: ")
        while (unaPatente in patentes) is False:
            unaPatente = input("Patente no encontrada, ingrese nuevamente: ")
        print("Moto encontrada. Ingrese los siguientes datos: ")
        idPedido = input("Identificador del pedido: ")
        comidas = input("Comidas: ")
        tiempoEst = input("Tiempo estimado: ")
        tiempoReal = input("Tiempo real: ")
        precio = float(input("Precio: "))
        unPedido = Pedido(unaPatente, idPedido, comidas, tiempoEst, tiempoReal, precio)
        self.agregarPedido(unPedido)
    def modificarTiempo(self):
        i = 0
        patente = input("Ingrese patente: ")
        idPedido = input("Ingrese el identificador de pedido: ")
        tiempoReal = input("Ingrese nuevo tiempo real: ")
        bandera = False
        while bandera is False and i < len(self.__ListaPedidos):
            if self.__ListaPedidos[i].getId() == idPedido:
                bandera = not bandera
                self.__ListaPedidos[i].setTiempoReal(tiempoReal)
            else:
                i += 1
        if bandera == False:
            print("Pedido no encontrado")
    def mostrarDatos(self, mm):
        total = 0
        cont = 0
        patente = input("Ingrese una patente a buscar: ")
        datos = mm.getDatos(patente)
        if datos != -1:
            for unPedido in self.__ListaPedidos:
                if unPedido.getPatente() == patente:
                    total += unPedido.getTiempoReal()
                    cont += 1
            print("Datos")
            print(f"Nombre: {datos[0]}")
            print(f"Apellido: {datos[1]}")
            print(f"Marca: {datos[2]}")
            print(f"Kilometraje: {datos[3]}")
            print(f"Promedio de tiempo Real: {total/cont}")
        else:
            print("Patente no encontrada")
    def generarListado(self, conductores, patentes):
        for i in range(len(patentes)):
            xcon = conductores[i]
            xpat = patentes[i]
            total = 0
            print(f"""Comisiones para la moto {i+1}:\nPatente de la moto: {xpat}\nConductor: {xcon}\nId del pedido   Tiempo estimado   Tiempo Real   Precio""")
            for unPedido in self.__ListaPedidos:
                if unPedido.getPatente() == xpat:
                    idPedido = unPedido.getId()
                    tiempoEst = unPedido.getTiempoEst()
                    tiempoReal = unPedido.getTiempoReal()
                    precio = unPedido.getPrecio()
                    total += precio
                    print(f"       {idPedido}            {tiempoEst}             {tiempoReal}         {precio}")
            print(f"Total: ${round(total, 2)}")
            print(f"Comision: ${round((total*20)/100, 2)}\n")