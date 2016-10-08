'''
Created on 29/8/2016

@author: javier_zardain

- Se requiere ingresar por pantalla materias de la carrera. La materia se compone con: numero de 5 cifras de identificacion unica, un nombre y un listado de alumnos (con sus notas).
'''
codigo = 11111
listaMaterias = {}


def ingresarAlumno(listaAlumnos):
    alumno = input("Ingrese el nombre del alumno: ")
    while(len(alumno)< 5):
        alumno = input("Ingrese el nombre del alumno (Minimo 5 caracteres): ")
    listaAlumnos.update({alumno : {"notas" : [], "promedio":0}})
    
def ingresarNota(listaAlumnos):
    for alumno, valor in listaAlumnos.items():
        print(alumno)
    alumno = listaAlumnos[input("Ingrese el nombre del alumno: ")]
    seguir= True
    while(seguir):
        nota = int(input("Ingrese la nota del alumno: "))
        while(nota > 10 or nota < 0):
            nota = input("Ingrese la nota del alumno (0 - 10): ")
        alumno["notas"].append(nota)
        promedio = 0
        j = 0
        for nota in alumno["notas"]:
            promedio = promedio + nota
            j += 1
        alumno["promedio"] = promedio / j
        if(input("Desea continuar s/n?") == "s"):
            seguir = True
        else:
            seguir = False
            
def listarAlumnos(listaAlumnos):
    for alumno,valor in listaAlumnos.items():
        print("-------------------------")
        print("Alumno:")
        print(alumno)
        print("Notas:")
        print(valor["notas"])
        print("Promedio:")
        print(valor["promedio"])
        print("-------------------------")
        
def ingresarMateria():
    nombreMateria = input("Ingrese el nombre de la materia: ")
    code = codigo + 1
    materia = {"codigo":code, "listaAlumnos":{}}
    listaMaterias[nombreMateria]=materia
    return materia
    
if __name__ == "__main__":
    listaAlumnos = {}
    funciones = [ingresarAlumno, ingresarNota,listarAlumnos]
    materia = ingresarMateria()
    while(True):
        print("1 - Ingresar alumno")
        print("2 - Ingresar notas")
        print("3 - Lista de alumnos")
        opcion = input("Ingrese una opcion: ")
        funciones[int(opcion)-1](materia["listaAlumnos"])
    
    
    