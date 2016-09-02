#5- Se debera generar un sistema que mantenga en memoria datos de una agenda.
#    - El programa mostrara las opciones> agregar, editar, borrar, mostrar y salir
#    agregar, agenda un contacto (email, telefono, nombre, domicilio, edad y dni)
#    editar, permite modificar cualquiera de los contactos seleccionando su email.
#    borrar, elimina un contacto.
opcion = int(input("Ingrese 1 para agregar, 2 para editar, 3 para borrar, 4 para mostrar y 5 para salir"))
diccionario = {}
while opcion != 5:
    if opcion == 1:
        email = input("ingrese un email")
        if diccionario.__contains__(email):
            print("Error! Ya existe este email")
        else:
            telefono = input("ingrese un telefono")
            nombre = input("ingrese un nombre")
            domicilio = input("ingrese un domicilio")
            edad = input("ingrese una edad")
            dni = input("ingrese un dni")
            diccionario[email] = {"telefono": telefono, "nombre": nombre, "domicilio": domicilio, "edad": edad, "dni": dni}
    elif opcion == 2:
        email = input("Ingrese el email del contacto que quiere editar")
        if not diccionario.__contains__(email):
            print("Error! no existe este email")
        else:
            diccionario[email]["telefono"] = input("ingrese un telefono")
            diccionario[email]["nombre"] = input("ingrese un nombre")
            diccionario[email]["domicilio"] = input("ingrese un domicilio")
            diccionario[email]["edad"] = input("ingrese una edad")
            diccionario[email]["dni"] = input("ingrese un dni")
    elif opcion == 3:
        email = input("Ingrese el email del contacto que quiere borrar")
        if not diccionario.__contains__(email):
            print("Error! no existe este email")
        else:
            diccionario.pop(email)
    elif opcion == 4:
        email = input("Ingrese el email del contacto que quiere mostrar")
        if not diccionario.__contains__(email):
            print("Error! no existe este email")
        else:
            print("telefono: " + diccionario[email]["telefono"])
            print("nombre: " + diccionario[email]["nombre"])
            print("domicilio: " + diccionario[email]["domicilio"])
            print("edad: " + diccionario[email]["edad"])
            print("dni: " + diccionario[email]["dni"])
    opcion = int(input("Ingrese 1 para agregar, 2 para editar, 3 para borrar, 4 para mostrar y 5 para salir"))  