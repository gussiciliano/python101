
'''
Created on 29/8/2016

@author: javier_zardain

- Se requiere ingresar por pantalla notas de alumnos y sus respectivos nombres. Los nombres deberan contener minimamente 5 caracteres y su nota sera entre 0 y 10.
Es necesario calcular el promedio de los alumnos.
'''


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
        
if __name__ == "__main__":
    listaAlumnos = {}
    funciones = [ingresarAlumno, ingresarNota,listarAlumnos ]
    while(True):
        print("1 - Ingresar alumno")
        print("2 - Ingresar notas")
        print("3 - Lista de alumnos")
        opcion = input("Ingrese una opcion: ")
        funciones[int(opcion)-1](listaAlumnos)
    
    
    