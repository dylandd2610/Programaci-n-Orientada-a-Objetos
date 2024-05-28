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

def test(Lista):
    for i in range(3):
        print(f"\nIngrese los siguientes datos para el objeto Num {i+1}")
        numC = input("numero de cuenta: ")
        cuil = input("cuil sin guion: ")
        ape = input("apellido: ")
        nom = input("nombre: ")
        saldo = float(input("saldo: "))
        Lista.append(CajadeAhorro(numC, cuil, ape, nom, saldo))

if __name__ == '__main__':
    Lista = []
    test(Lista)  
    for i in range(3):
        imp = float(input("Ingrese un importe para extraer: "))
        val = Lista[i].extraer(imp)
        if val == -1: 
            print("\nNo se pudo realizar la extraccion")
        else:
            print(f"Si se pudo reaizar la extraccion\nNuevo Saldo:{val}")
        ximp = float(input("Ingrese un importe para depositar: "))
        Lista[i].depositar(ximp)
        Lista[i].validarCUIL()