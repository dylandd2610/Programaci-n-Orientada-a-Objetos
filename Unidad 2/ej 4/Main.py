import csv
from ManejadorMotos import ManejadorMotos
from ManejadorPedidos import ManejadorPedidos

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