class Ladrillo:
    alto = 7
    largo = 25
    ancho = 15
    __cant: int
    __Id: int
    __kgMatprimUti: float
    __costo: float
    __listaMateriales: list
    def __init__(self, cant, Id, kg, costo):
        self.__cant = cant
        self.__Id = Id
        self.__kgMatprimUti = kg
        self.__costo = costo
        self.__listaMateriales = []
    def __str__(self):
        return "%s %s %s %s" % (self.__cant, self.__Id, self.__kgMatprimUti, self.__costo)
    def agregarMaterial(self, unMaterial):      #agrega un material a la lista de materiales
        self.__listaMateriales.append(unMaterial)
    def mostrarListaMat(self):          #muestra la lista de materiales
        print("Materiales")
        for material in self.__listaMateriales:
            print(f"    [{material}]")
    def getCant(self):
        return self.__cant
    def getId(self):
        return self.__Id
    def getKgMatpimUti(self):
        return self.__kgMatprimUti
    def getCosto(self):
        return self.__costo
    @classmethod
    def getAlto(cls):
        return cls.alto
    @classmethod
    def getLargo(cls):
        return cls.largo
    @classmethod
    def getAncho(cls):
        return cls.ancho
    def informarDatos(self):     #informa material, costo y caracteristicas de un material
        if len(self.__listaMateriales)>0:
            print("Material        Costo         Caracteristicas")
            for material in self.__listaMateriales:
                print(f"    {material.getMaterial()}           {material.getCosto()}         {material.getCaract()}")
        else:
            print("Este ladrillo no usa material refractario")
    def calcularTotal(self):    #calcula el costo total de fabricacion
        total = self.__costo
        for material in self.__listaMateriales:
            total += material.getCosto()
        return total
    def contarMat(self):    #suma todos los materiales en un cadena
        cadena = ""
        i = 1
        if len(self.__listaMateriales)>0:
            for material in self.__listaMateriales:
                i += 1
                if i > len(self.__listaMateriales):
                    cadena += str(material.getMaterial())
                else:
                    cadena += str(material.getMaterial())+", "
        return cadena
    def costoAdicional(self):       #suma el costo adicional de cada material
        total = 0.0
        if len(self.__listaMateriales)>0:
            for material in self.__listaMateriales:
                total += material.getCosto()
        return total