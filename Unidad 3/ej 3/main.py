from gestorEmpleados import GestorEmpleados
from gestorProgramas import GestorProgramas
from gestorMatriculas import GestorMatriculas
def test():
    op = None
    try:
        op = int(input("""
    ________________________________________Menu de opciones________________________________________
                1_Informar programas de capacitacion en los que esta matriculado un empelado
                2_Informar empleados capacitados en un programa de capacitacion
                3_Informar empleados que no han sido matriculados en ningun programa de capacitacion
                4_Mostrar listado de empleados
                5_Mostrar listado de programas de capacitacion
                6_Mostrar listado de matriculas
                0_Salir
                --> """))
    except ValueError:
        pass
    return op
if __name__ == '__main__':
    ge = GestorEmpleados()
    gp = GestorProgramas()
    gm = GestorMatriculas()
    ge.testEmpleados()
    gp.testProgramas()
    gm.testMatriculas(ge, gp)
    op = test()
    while op != 0:
        if op == 1:
            try:
                Id1 = int(input("Ingrese un Id de empleado: "))
                ge.informarDuracionProgramas(Id1)
            except ValueError:
                print("Error. Se esperaba un numero entero")
            except AssertionError:
                print("Error. El empleado solicitado no existe")
        elif op == 2:
            try:
                nomP = input("Ingrese el nombre de un programa de capacitacion: ")
                gp.informarEmpleadosMat(nomP)
            except AssertionError:
                print("Error. El programa solicitado no existe")
        elif op == 3:
            ge.informarNoMatriculados(gm)
        elif op == 4:
            ge.mostrarEmpleados()
        elif op == 5:
            gp.mostrarProgramas()
        elif op == 6:
            gm.mostrarMatriculas()
        else:
            print("Opcion Incorrecta. Ingrese nuevamente")
        op = test()
    print("________________________________________Finalizacion del programa________________________________________")