#3- Se requiere ingresar por pantalla materias de la carrera. 
#La materia se compone con: numero de 5 cifras de identificacion unica, un nombre y un listado de alumnos (con sus notas).
accion = input("Pressione S para ingresar un materia, cualquir otra letra para terminar")
diccionarioMaterias = {}
while accion == "S":
    identificacion = input("Ingrese el id")
    while len(identificacion) > 5:
        identificacion = input("Error! El id debe ser de 5 cifras. Ingrese el id")
    nombre = input("Ingrese el nombre de la materia, luego va a ingresar los alumnos")
    from Clase2 import Ejericio2
    from Clase2.Ejericio2 import diccionario
    diccionarioMaterias[identificacion]={nombre:diccionario}
    accion = input("Pressione S para ingresar un materia, cualquir otra letra para terminar")