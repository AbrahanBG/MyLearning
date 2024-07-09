#Polimorfismo

#class Auto():
    #rueda = 4

    #def desplazamiento(self):
        #print('El auto se va moviendo en 4 ruedas')

#class Moto():
    #rueda = 2

    #def desplazamiento(self):
        #print('El auto se va moviendo en 2 ruedas')


class Animales:
    def __init__(self,nombre):
        self.nombre= nombre

    def tipo_animal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print('Animal Salvaje')

class Perro(Animales):
    def tipo_animal(self):
        print('Animal Domestico')


nuevo_animal= Leon('Simba')
nuevo_animal.tipo_animal()   #mismo nombre de funcion diferente acciones
nuevo_animal2= Perro('Rex')
nuevo_animal2.tipo_animal()

############################################Polimorfis/Func/Metodo/Herencia#########################################

class Tomate():
    def tipo(self):
        print('vegetal')

    def color(self):
        print('rojo')

class Manzana():
    def tipo(self):
        print('fruta')

    def color(self):
        print('VERDE')

def function(objeto):
    objeto.tipo()
    objeto.color()

nuevo_tomate = Tomate()
function(nuevo_tomate)
nueva_manzana=Manzana()
function(nueva_manzana)


##############################################Polimorfis con Metodo

class Colombia:
    def Capital(self):
        print('Bogota')
    def Idioma(self):
        print('Español')

class Francia:
    def Capital(self):
        print('Paris')
    def Idioma(self):
        print('Frances')

colombiano = Colombia()
frances = Francia()

for pais in (colombiano,frances):
    pais.Capital()
    pais.Idioma()


##################################################pPolimorfismo con Herencia

class Ave:
    def volar(self):
        print('La mayoria de las aves puden volar pero alguna no')

class Aguila(Ave):
    def volar(self):
        print('Estas si vuelan')

class Gallino(Ave):
    def volar(self):
        print('esta no puede volar')

obj_ave = Ave()
obj_ave.volar()
obj_aguila = Aguila()
obj_aguila.volar() 
obj_gallina = Gallino()
obj_gallina.volar() 





