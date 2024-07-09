class Persona:
    edad = 27
    nombre = 'victor'
    pais = 'brasil'

doctor = Persona()

print(doctor.edad)
print('la edad es:',getattr(doctor,'edad'))
print('doctor tiene apellido:',hasattr(doctor,'apellido'))
setattr(doctor,'nombre','pancho')
print(doctor.nombre)
delattr(Persona,'pais')
print('Atributo edad existe',hasattr(Persona,'pais'))
