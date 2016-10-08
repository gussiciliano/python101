'''
Created on 31/8/2016

@author: javier_zardain

- Se debera generar un sistema que mantenga en memoria datos de una agenda.
- El programa mostrara las opciones> agregar, editar, borrar, mostrar y salir
agregar, agenda un contacto (email, telefono, nombre, domicilio, edad y dni)
editar, permite modificar cualquiera de los contactos seleccionando su email.
borrar, elimina un contacto.
'''
import sys

def agregarContacto(listaContactos):
    nombre = input("Nombre: ")
    dni = input("Dni: ")
    edad = input("Edad: ")
    domicilio = input("Domicilio: ")
    telefono = input("Telefono: ")
    email = input("Email: ")
    listaContactos[email]={"nombre":nombre, "dni":dni, "edad":edad, "domicilio": domicilio, "telefono":telefono}
    
def editarContacto(listaContactos):
    email = input("Email del contacto: ")
    print(listaContactos[email])
    print("Que desea modificar?")
    opciones ="1-Nombre \n 2-Dni \n 3-Edad \n 4-Domicilio \n 5-Telefono \n 6-Salir"
    print(opciones)
    opcion = input("Escoja una opcion: ")
    if(opcion!="6"):
        seleccion = opciones[opciones.index(opcion)+2:opciones.index(" ")].lower()
        listaContactos[email][seleccion] = input("Introduzca el nuevo " + seleccion + ": ")
    
def borrarContacto(listaContactos):
    for Email,valor in listaContactos.items():
        print(Email)
    email = input("Email del contacto: ")
    print(listaContactos.pop(email,None))
    
def mostrarContactos(listaContactos):
    for Email,valor in listaContactos.items():
        print("-------------------------")
        print("Email:")
        print(Email)
        print("Nombre:")
        print(valor["nombre"])
        print("Dni:")
        print(valor["dni"])
        print("Edad:")
        print(valor["edad"])
        print("Domicilio:")
        print(valor["domicilio"])
        print("Telefono:")
        print(valor["telefono"])
        print("-------------------------")

if __name__ == "__main__":
    listaContactos = {}
    funciones = [agregarContacto, editarContacto,borrarContacto, mostrarContactos]
    while(True):
        print("1 - Ingresar contacto")
        print("2 - Editar contacto")
        print("3 - Borrar contacto")
        print("4 - Mostrar contactos")
        print("5 - Salir")
        opcion = input("Ingrese una opcion: ")
        if(opcion == "5"):
            sys.exit()
        funciones[int(opcion)-1](listaContactos)