#Clase plantilla para crear objetos Ejemplo Plano de Casa
#Ibnstancia es un objeto que se crea usando el cosntructor de una clase, una vez que el objeto se le crea es conocido como instancia de clase
#Metodos Estatics, Metodos de Clase, Instancia


##########Metodo de  Clasee###############
#Estre metodo puede ser llamado sin crear una instancia de clase

class Pastel:
    def __init__(self,ingredientes):
        self.ingredientes = ingredientes

    def __repr__(self):
        return f'pastel({self.ingredientes !r})'
    
    @classmethod
    def Pastel_Chocolate(cls):
        return cls(['Harina','Harina','Chocolate'])
    
    @classmethod
    def Pastel_Vainilla(cls):
        return cls(['Harina','Harina','Vainilla'])
    

print(Pastel.Pastel_Chocolate())



###################################################Metodo Estatico
#Pueden ser llamadas sin tener una instancia de la clase, ademas no tienen acceso al exterior
import math
    
class Pastel1:
    def __init__(self,ingredientes,tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño

    def __repr__(self):
        return (f'pastel({self.ingredientes}, 'f'{self.tamaño})')
    
    def area(self):
        return self.tamaño_area(self.tamaño)
    
    @staticmethod
    def tamaño_area(A):
        return A * 2 * math.pi
    
nuevo_pastel = Pastel1(['Harina','Leche','chispas'], 4)
print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamaño)
print(nuevo_pastel.area())
print(nuevo_pastel.tamaño_area(5))