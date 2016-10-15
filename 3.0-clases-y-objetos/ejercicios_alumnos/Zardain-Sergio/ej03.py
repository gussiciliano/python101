# -*- coding: utf-8 -*-

'''
    @note: Se requiere modelar un "contacto" con clases (debe poseer los mismos datos que ejercicio de 1.5).

Se debera generar un sistema que mantenga en memoria datos de una agenda.
    - El programa mostrara las opciones> agregar, editar, borrar, mostrar y salir
    agregar, agenda un contacto (email, telefono, nombre, domicilio, edad y dni)
    editar, permite modificar cualquiera de los contactos seleccionando su email.
    borrar, elimina un contacto.

'''



class Contacto:
    def __init__(self):
        email = ""
        telefono = 0
        nombre = ""
        domicilio = ""
        edad = 0
        dni = 0
    
    def agregar(self):
        
        self.email = str(input("Email: "))
        self.telefono = input("Tel: ")
        self.nombre = input(" nom")
        self.domicilio = input("domici: ")
        self.edad = int(input("Edad: "))
        self.dni = int(input("dni: "))
    
    def editar(self):
        
        pass
    
    def borrar(self):
        
        pass
    
    def mostrar(self):
        
        pass

if __name__ == "__main__":
    
    
    
    micontacto = Contacto()
    
    micontacto.agregar()