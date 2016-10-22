'''
Created on Sep 10, 2016

@author: python
'''

def recoleccionDeDatos():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = int(input("Ingrese el dni: "))
    telefono = int(input("Ingrese el telefono: "))
    email = input("Ingrese el email: ")
    domicilio = input("Ingrese el domicilio: ")
    fechaNacimiento = input("Ingrese la fecha de nacimiento separada por guiones (d-m-a): ")
    return  Contacto(nombre,apellido,telefono,email,dni,domicilio,fechaNacimiento)

class Contacto:

    def __init__(self, nombre, apellido, telefono, email, dni, domicilio,fechaNacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.dni = dni
        self.domicilio = domicilio
        self.fechaNacimiento = fechaNacimiento
    