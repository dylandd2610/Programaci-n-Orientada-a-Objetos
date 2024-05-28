class CajadeAhorro:
    __nroCuenta: str
    __cuil: str
    __apellido: str
    __nombre: str
    __saldo: float
    def __init__(self, nroCuenta, cuil, apellido, nombre, saldo = 0):
        self.__nroCuenta = nroCuenta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = saldo 
    
    def mostrarDatos(self):
        print(f"Nro de cuenta:{self.__nroCuenta}\nCuil:{self.__cuil}\nApellido:{self.__apellido}\nNombre:{self.__nombre}\nSaldo:{self.__saldo}")
        
    def extraer(self, imp):
        if self.__saldo >= imp:
            self.__saldo -= imp
            return self.__saldo
        else:
            return -1
        
    def depositar(self, ximp):
        if ximp > 0:
            print("Si es positivo")
            self.__saldo += ximp
            print(f"Nuevo saldo:{self.__saldo}")
        else:
            print("No es positivo")
    def validarCUIL(self):
        valores = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        sumatoria = 0
        Lista_xcuil = [int(caracter) for caracter in self.__cuil]
        XY = Lista_xcuil[:2]
        DNI= Lista_xcuil[2:10]
        num = Lista_xcuil[10:]
        Digito = int(num[0])
        if XY == [2, 0]:
            tipo = "Hombre"
        elif XY == [2, 7]:
            tipo = "Mujer"
        else:
            tipo = "Empresa o Sociedad"
        for i in range(10):
            sumatoria += Lista_xcuil[i] * valores[i]
        resto = sumatoria % 11
        if resto==0:
            if Digito == 0:
                print("Resto:", resto)
                print("Digito:", Digito)
                print("Cuil es valido")
        elif resto == 1:
            if tipo == "Hombre":
                if Digito == 9 and XY == 23:
                    print("Resto:", resto)
                    print("Digito:", Digito)
                    print("Cuil es valido")
            elif tipo == "Mujer":
                if Digito == 4 and XY == 23:
                    print("Resto:", resto)
                    print("Digito:", Digito)
                    print("Cuil es valido")
            else:
                print("Cuil es invalido")
        else:
            resto = 11 - resto
            if Digito == resto:
                print("Resto:", resto)
                print("Digito:", Digito)
                print("Cuil es valido")
            else:
                print("Cuil es invalido")
    
class Contenedor:
    __Lista: list
    def __init__(self, ):
        self.__Lista = []
    def agregarCuenta(self, unaCuenta):
        self.__Lista.append(unaCuenta)
    def mostrarCuentas(self):
        for cuenta in self.__Lista:
            cuenta.mostrarDatos()
    def ObtenerDatos(self, xcuil):
        i = 0
        encontrado = False
        while i < len(self.__Lista) and not encontrado:
            if xcuil == self.__Lista[i]._CajadeAhorro__cuil:
                encontrado = True
            i += 1
        if encontrado:
            self.__Lista[i-1].mostrarDatos()
        else:
            print("Cuil no valido")
            
def test(xlist):
    c1 = CajadeAhorro("3", "20460708304", "Nunez", "Dylan", 67546257)
    c2 = CajadeAhorro("2", "23291089704", "Delgado", "Monica", 42356223)
    c3 = CajadeAhorro("1", "20440188908", "Blanco", "Luca", 2114242)
    xlist.agregarCuenta(c1)
    xlist.agregarCuenta(c2)
    xlist.agregarCuenta(c3)
    return xlist

if __name__ == '__main__':
    listaCuentas = Contenedor()
    listaCuentas = test(listaCuentas)
    #listaCuentas.mostrarCuentas()
    cuil = input("\nIngrese cuil: ")
    listaCuentas.ObtenerDatos(cuil)