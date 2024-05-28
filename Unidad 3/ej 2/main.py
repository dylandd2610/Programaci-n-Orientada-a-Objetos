from gestorLadrillos import GestorLadrillo
from gestorMateriales import GestorMaterial
def test():
    op = None
    try:
        op = int(input("""
------------------------------Menu de opciones------------------------------
                1_Dado un Id de ladrillo, informar costo y caracteristicas de su/s material/es
                2_Informar costo total de fabricacion de cada ladrillo
                3_Informar detalles de cada ladrillo
                4_Mostrar listado de materiales
                5_Mostrar listado de ladrillos
                0_Salir
                --> """))
    except ValueError:
        pass
    return op
if __name__ == '__main__':
    gm = GestorMaterial()
    gm.testMateriales()
    gl = GestorLadrillo()
    gl.testLadrillos(gm)
    op = test()
    while op != 0:
        if op == 1:
            Id = int(input("Ingrese un id de un ladrillo: "))
            try:
                gl.InformarDatosLadrillo(Id)
            except ValueError:
                print("Error. Se esperaba un numero entero")
            except AssertionError:
                print(f"Error. El ladrillo de id {Id} no existe")
        elif op == 2:
            gl.mostrarCostoTotal()
        elif op == 3:
            gl.informarMaterial()
        elif op == 4:
            gm.mostrarMateriales()
        elif op == 5:
            gl.mostrarLadrillos()
        else:
            print("Opcion invalida. Ingrese nuevamente")
        op = test()
    print("------------------------------Finalizacion del Programa------------------------------")
'''
lote de prueba
1
2
3
0
4
5
0
1
5
0
0
2
5
1
0

'''