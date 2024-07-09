class Matematica:
    def suma(self):
        self.m1 = 2
        self.m2 = 3

s = Matematica()
s.suma()
#print(s.m1 + s.m2)

class Ropa:
    def __init__(self):
        self.marca = 'willow'
        self.talla = 'Mediana'
        self.color = 'rojo'

camisa = Ropa()
#print(camisa.talla)

class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1/n2

operacion = Calculadora(2,3)
print(operacion.producto)

