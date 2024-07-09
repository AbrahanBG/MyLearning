#f-string
#format %

curso ='python'
print("tutorial de % s" %curso)

nombre1 = 'victor'
edad1 = 25

print("Hola soy % s y tengo % s años."%(nombre1,edad1))
print(f"Hola soy {nombre1} y tengo {edad1} años.")

class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f'El nombre es: {self.nombre} {self.apellido} y tiene {self.edad} años.'
    
nuevoestudiante = Estudiante('Victor','Cruz',18)
print(nuevoestudiante)