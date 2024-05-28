import csv
class Moto: #clase moto
    __patente: str
    __marca: str
    __nombre: str
    __apellido: str
    __kilometraje: int
    def __init__(self, patente, marca, nombre, apellido, kilometraje):
        self.__patente = patente
        self.__marca = marca
        self.__nombre = nombre
        self.__apellido = apellido
        self.__kilometraje = kilometraje
    def __str__(self):
        return "%s %s %s %s %s" % (self.__patente, self.__marca, self.__nombre, self.__apellido, self.__kilometraje)
    def getPatente(self):
        return self.__patente
    def getMarca(self):
        return self.__marca
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getKilometraje(self):
        return self.__kilometraje

class Pedido: #clase pedido
    __patente: str
    __idPedido: int
    __comidas: str
    __tiempoEst: int
    __tiempoReal: int
    __precio: float
    def __init__(self, patente, idPedido, comidas, tiempoEst, tiempoReal, precio):
        self.__patente = patente
        self.__idPedido = idPedido
        self.__comidas = comidas
        self.__tiempoEst = tiempoEst
        self.__tiempoReal = tiempoReal
        self.__precio = precio
    def __str__(self):
        return "%s %s %s %s %s %s" % (self.__patente, self.__idPedido, self.__comidas, self.__tiempoEst, self.__tiempoReal, self.__precio)
    def getPatente(self):
        return self.__patente
    def getId(self):
        return self.__idPedido
    def getComidas(self):
        return self.__comidas
    def getTiempoEst(self):
        return self.__tiempoEst
    def getTiempoReal(self):
        return int(self.__tiempoReal)
    def getPrecio(self):
        return float(self.__precio)
    def setTiempoReal(self, tiempoR):
        self.__tiempoReal = tiempoR
    def __lt__(self, otro):
        return self.__patente < otro.getPatente()

class ManejadorMotos:
    def __init__(self):
        self.__ListaMotos = []
    def agregarMoto(self, unaMoto):
        self.__ListaMotos.append(unaMoto)
    def mostrarLista(self):
        for moto in self.__ListaMotos:
            print(f"[{moto}]")
    def testMoto(self):
        archivo = open('datosMotos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                patente = fila[0]
                marca = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                kilometraje = int(fila[4])
                unaMoto = Moto(patente, marca, nombre, apellido, kilometraje)
                mm.agregarMoto(unaMoto)
        archivo.close()
    def getListaPatentes(self):
        lista = []
        for i in self.__ListaMotos:
            lista.append(i.getPatente())
        return lista
    def getDatos(self, patente):
        bandera = False
        lista = []
        i = 0
        while bandera is False and i<len(self.__ListaMotos):
            if self.__ListaMotos[i].getPatente() == patente:
                lista.append(self.__ListaMotos[i].getNombre())
                lista.append(self.__ListaMotos[i].getApellido())
                lista.append(self.__ListaMotos[i].getMarca())
                lista.append(self.__ListaMotos[i].getKilometraje())
                bandera = not bandera
            else:
                i += 1
        if bandera is False:
            return -1
        else: 
            return lista
    def getConductor(self):
        lista = []
        for i in self.__ListaMotos:
            lista.append(i.getNombre())
        return lista
            

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
                mp.agregarPedido(unPedido)
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
        mp.agregarPedido(unPedido)
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
            
        

if __name__ == '__main__':
    opcion = input("""   -------------Menu de opciones-------------
Ingrese una de las siguientes opciones:
1_Cargar datos de motos desde un archivo csv a un gestor
2_Cargar datos de pedidos desde un archivo csv a un gestor
3_Cargar nuevos pedidos al gestor
4_Modificar tiempo real de entrega de un pedido
5_Mostrar datos de u conductor y tiempo promedio real de entrega de sus pedidos
6_Generar listado de motos con pago de comisiones
7_Mostrar listado de motos
8_Mostrar listado de pedidos
0_Salir
-> """)
    while opcion != "0":
        if opcion == "1":
            mm = ManejadorMotos()
            mm.testMoto()
            conductores = mm.getConductor()
        elif opcion == "2":
            mp = ManejadorPedidos()
            mp.testPedidos()
            mp.ordenar()
            patentes = mm.getListaPatentes()
        elif opcion == "3":
            mp.cargaPedido(patentes)
        elif opcion == "4":
            mp.modificarTiempo()
        elif opcion == "5":
            mp.mostrarDatos(mm)
        elif opcion == "6":
            mp.generarListado(conductores, patentes)
        elif opcion == "7":
            print("Lista de motos:")
            mm.mostrarLista()
        elif opcion == "8":
            print("Lista de pedidos:")
            mp.mostrarLista()
        opcion = input("""-------------Menu de opciones-------------
Ingrese una de las siguientes opciones:
1_Cargar datos de motos desde un archivo csv a un gestor
2_Cargar datos de pedidos desde un archivo csv a un gestor
3_Cargar nuevos pedidos al gestor
4_Modificar tiempo real de entrega de un pedido
5_Mostrar datos de u conductor y tiempo promedio real de entrega de sus pedidos
6_Generar listado de motos con pago de comisiones
7_Mostrar listado de motos
8_Mostrar listado de pedidos
0_Salir
-> """)
    if opcion == "0":
        print("Finalizo el programa")