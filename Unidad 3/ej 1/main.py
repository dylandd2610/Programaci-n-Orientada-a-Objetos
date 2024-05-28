from gestorEdificio import GestorEdificio

def test():
    op = None
    try:
        op = int(input("""                  Menu de opciones
            1_Mostrar nombre y apellido de los propietarios de departamentos de un edificio.
            2_Mostrar la superficie total cubierta de un edificio. 
            3_Mostrar la superficie total cubierta de un departamento y el porcentaje representa del total del edificio.
            4_Mostrar la cantidad de departamentos que tienen 3 dormitorios y más de un baño.
            5_Mostrar lista de edificios y sus departamentos.
            0_Salir
            --> """))
    except ValueError:
        pass
    return op

if __name__ == '__main__':
    ge = GestorEdificio()
    ge.testEdificios()
    opcion = test()
    while opcion != 0:
        if opcion == 1:
            try:
                nomE1 = input("Ingrese un nombre de edificio: ")
                ge.mostrarPropietarios(nomE1)
            except TypeError as e:
                print(e)
        elif opcion == 2:
            try:
                nomE2 = input("Ingrese un nombre de edificio: ")
                ge.mostrarTotalSuper(nomE2)
            except TypeError as e:
                print(e)
        elif opcion == 3:
            try:
                nomP = input("Ingrese el nombre y apellido de un propietario: ")
                ge.indicarSuperficie(nomP)
            except AssertionError:
                print("Error. Propietario no encontrado")
        elif opcion == 4:
            try:
                numP = int(input("Ingrese un numero de piso: "))
                ge.informaCantDepa(numP)
            except AssertionError:
                print("Error. No existe ese numero de piso")
            except ValueError:
                print("Error. Se esperaba un numero entero")
        elif opcion == 5:
            ge.mostrarEdificioDepa()
        else:
            print("Opcion incorrecta")
        opcion = test()
    print("Finalizo el programa")