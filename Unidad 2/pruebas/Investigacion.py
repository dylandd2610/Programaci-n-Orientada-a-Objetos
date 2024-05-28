import numpy as np

class Matriz:
    __matriz: np.ndarray
    def __init__(self, matriz):
        self.__matriz = np.array(matriz) 

    def calcular_inversa(self):
        m_inv = np.linalg.inv(self.__matriz)
        return m_inv
    
    def multiplicacion(self, xm_inv):
        xmatriz = np.dot(self.__matriz, xm_inv)
        return xmatriz
    
    def mostrar(self):
        print(self.__matriz)
        
    
def test():
    #Crea una instancia de la clase Matriz cargada con datos
    datos_matriz = [[8, 2, 1], [1, 3, 1], [4, 2, 1]]
    matriz = Matriz(datos_matriz)
    
    #Calcula la inversa
    m_inv = matriz.calcular_inversa()
    
    #Muestra el resultado
    print(m_inv)
    
    #Multiplica la matriz original por la inversa y se obtiene la matriz identidad
    xmatriz = matriz.multiplicacion(m_inv)
    print(xmatriz)
    
if __name__ == '__main__':
    test()