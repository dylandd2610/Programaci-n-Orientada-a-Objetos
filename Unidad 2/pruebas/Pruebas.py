def validarCUIL(xcuil):
        valores = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        sumatoria = 0
        Lista_xcuil = [int(caracter) for caracter in xcuil]
        XY = Lista_xcuil[:2]
        print(XY)
        DNI= Lista_xcuil[2:10]
        num = Lista_xcuil[10:]
        Digito = int(num[0])
        print("Digito:",Digito)
        if XY == [2, 0]:
            tipo = "Hombre"
        elif XY == [2, 7]:
            tipo = "Mujer"
        else:
            tipo = "Empresa o Sociedad"
        print(tipo)
        for i in range(10):
            sumatoria += Lista_xcuil[i] * valores[i]
        print("Sumatoria:",sumatoria)
        resto = sumatoria % 11
        print("Resto1:", resto)
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
            if tipo == "Mujer":
                if Digito == 4 and XY == 23:
                    print("Resto:", resto)
                    print("Digito:", Digito)
                    print("Cuil es valido")
        else:
            resto = 11 - resto
            if Digito == resto:
                print("Resto:", resto)
                print("Digito:", Digito)
                print("Cuil es valido")

                
if __name__== '__main__':
    xcuil = input("Ingrese su numero de cuil(sin '-'): ")
    validarCUIL(xcuil)