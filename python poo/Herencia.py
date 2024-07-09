#crear nueva calase a partir de una ya existente

#class NombreSubClase(NombreClaseSuperior):
    #pass

#class ClaseBase:
    #pass
    #Cuerpo Clase


#class DerivadoClase(ClaseBase):
    #pass
    #Cuerpo de Clase Derivada


class Pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre 
        self.tipo = tipo
    
    def Descripcion(self):
        return '{} es un pokemon tipo: {}'.format(self.nombre,self.tipo)
    
class Pikachu(Pokemon):
    def ataque(self,tipoataque):
        return '{} tipo de ataque {}'.format(self.nombre, tipoataque)

class Charmander(Pokemon):
    def ataque(self,tipoataque):
        return '{} tipo de ataque {}'.format(self.nombre, tipoataque)
    
nuevo_pokemon = Pikachu('pepino','electrico')
#print(nuevo_pokemon.Descripcion())
#print(nuevo_pokemon.ataque('impacto trueno'))


class Calculadora():
    def __init__(self,numeros):
        self.numeros = numeros
        self.datos = [0 for i in range(numeros)]

    def ingresardatos(self):
        self.datos = [int(input('ingresar datos '+ str(i + 1)+ '=')) for i in range(self.numeros)]

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def Suma(self):
        a,b, = self.datos
        s = a + b
        print('el resultado es' , s)

    def Resta(self):
        a,b, = self.datos
        s = a- b
        print('el resultado es' , s)

    def Division(self):
        a,b = self.datos
        s = a/ b
        print('el resultado es',  s)

    def Producto(self):
        a,b = self.datos
        s = a* b
        print('el resultado es', s)

class Sqr(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def cuadrada(self):
        import math
        a, = self.datos
        print('La raiz es: ', math.sqrt(a))

ejemplo = Sqr()
#print(ejemplo.ingresardatos())
#print(ejemplo.cuadrada())

objeto = op_basicas()
#print(isinstance(objeto, op_basicas))
#print(issubclass(Calculadora,op_basicas))


##########################################------Herencia Multiple  --------------###################################3

#class Base_uno:
    #pass

#class Base_dos:
    #pass

#class DerivadoMultiple(Base_uno,Base_dos):
    #pass


class Telefono():
    def __init__(self):
        pass

    def Llamar(self):
        print('Llamando...')

    def Busy(self):
        print('Ocupado...')

class Camara:
    def __init__(self):
        pass

    def fotografia(self):
        print('tomando fotos...')

class Reproduccion():
    def __init__(self):
        pass

    def Music(self):
        print ('reproduciendo peso pluma')

    def Video(self):
        print('Reproduciendo intendsamente')

class Smartphone(Telefono,Camara,Reproduccion):
     def __del__(self):
         print('Telefono Apagado...')


movil = Smartphone()
print(movil.fotografia())
print(movil.Llamar())
print(movil.Music())