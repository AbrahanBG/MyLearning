class Mamifero:
    def __init__(self, nombre):
        print(nombre, 'Animal de sangre caliente')

class Leon(Mamifero):
    def __init__(self):
        print('El leon esta chido')
        super().__init__('simba')
        Mamifero.__init__(self,'simba') #como en herencia multiple

nuevoleon = Leon()