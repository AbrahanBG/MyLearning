#Encapsulacion

class Cliente:
    def __init__(self):
        self.__codigo = 4321

    def __cuenta(self):
        print('cuenta de proicesamiento')

    def get_codigo(self):
        return self.__codigo
    

persona = Cliente()
#print(hasattr(persona,'get_codigo')) Validar que si se encuentre el att
#print(hasattr(persona,'__cuenta')) Validar que si se esconda el ATT

#objeto.__nombreclase__nombreatributo
#print(persona._Cliente__codigo())
print(persona._Cliente__cuenta())

