#2- Se requiere ingresar por pantalla notas de alumnos y sus respectivos nombres. 
#Los nombres deberan contener minimamente 5 caracteres y su nota sera entre 0 y 10.
#Es necesario calcular el promedio de los alumnos.
accion = input("Pressione S para ingresar un alumno, cualquir otra letra para terminar")
diccionario = {}
while accion == "S":
    alumno = input("Ingrese el nombre el alumno")
    while len(alumno) > 5:
        alumno = input("Error! Los nombres deben contener minimamente 5 caracteres. Ingrese el nombre el alumno")
    nota = input("Ingrese su nota")
    while int(nota) < 0 or int(nota) > 10:
        nota = input("Error! La nota debe ser entre 0 y 10. Ingrese su nota")
    diccionario[alumno]=nota
    accion = input("Pressione S para ingresar un alumno, cualquir otra letra para terminar")
i=0
promedio = 0
for nombre, nota in diccionario.items():
    promedio+=int(nota)
    i+=1
if i>0:
    print(promedio/i)