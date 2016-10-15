# -*- coding: utf-8 -*-
#!/usr/local/bin/python3.5
import random

'''
funcion que retorna una lista de alumnos cargados
'''
def cargarAlumnos():
    diccionarioAlumnos = {}
    nombreAlumno = ""
    notaAlumno = 0
    rta = "y"
    while("y" in str(rta).lower() ):
        while(True): # valido los caracteres del nombre
            nombreAlumno = input("        Ingrese nombre del alumno: ")
            if len(nombreAlumno) < 5:
                print("El nombre debera contener 5 caracteres como minimo.")
            else:
                break
        while(True): # valido la longitud de la nota
            notaAlumno = float(input("        Ingrese la nota del alumno: "))
            if (notaAlumno >= 0 and notaAlumno <= 10) == False:
                print("La nota debe estar entre 0 y 10.")
            else:
                break
        diccionarioAlumnos[nombreAlumno] = notaAlumno # asigno el alumno al diccionario
        print(" ")
        rta = str(input("Desea cargar mas alumnos? (y/n)"))
    return diccionarioAlumnos

'''
funcion que retorna una lista de materias con sus alumnos asociados
'''
def cargarMaterias():
    nombreMateria = ""
    idMateria = 0
    diccionarioMaterias = {}
    diccionarioAlumnos = {}
    rta = "y"
    while("y" in str(rta).lower() ):
        nombreMateria = str(input("    Ingrese nombre de la Materia: "))
        while (True):
            idMateria = int(str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)))
            if not idMateria in diccionarioMaterias.keys():
                break
        # llamo a la funcion que carga todos los alumnos
        diccionarioAlumnos = cargarAlumnos()
        diccionarioMaterias[idMateria] = {"nombreMateria":nombreMateria,"alumnos":diccionarioAlumnos}
        print(" ")
        rta = str(input("Desea cargar mas materias? (y/n)"))
    return diccionarioMaterias

'''
funcion que retorna una lista de carreras con materias asociadas que tienen alumnos
'''
def cargarCarreras():
    diccionarioCarreras = {}
    diccionarioMaterias = {}
    listaCarreras = []
    nombreCarrera = ""
    rta = "y"
    while("y" in str(rta).lower() ):
        # Ingreso una nueva carrera
        nombreCarrera = str(input("Ingrese nombre de la carrera: "))
        # llamo una funcion que carga todo lo demas
        diccionarioMaterias = cargarMaterias()
        # cargo un diccionario de carreras con materias ya ingresadas
        diccionarioCarreras[nombreCarrera] = diccionarioMaterias
        # agrego la carrera dentro de la lista de carreras
        listaCarreras.append(diccionarioCarreras)
        print(" ")
        rta = str(input("Desea cargar mas carreras? (y/n)"))
    return listaCarreras

'''
muestro toda las carreras
'''
def mostrarCarreras(listaCarreras):
    print("*** CARGA DE CARRERAS ****")
    for carrera in listaCarreras:
        print("*** CARRERAS ***")
        for nomCarrera, dicCarreras in carrera.items():
            print("Nombre Carrera: " + nomCarrera)
            print("    *** MATERIAS ***")
            for codMateria,dicMaterias in dicCarreras.items():
                print("    Cod Materia: " + str(codMateria))
                print("    Materia: " + dicMaterias["nombreMateria"])
                print("        *** ALUMNOS ***")
                for nombre, nota in dicMaterias["alumnos"].items():
                    print("        Nombre: " + nombre)
                    print("        Nota: " + str(nota))

if __name__ == "__main__":

    listaCarreras = []
    #llamo a una funcion que carga las carreras con sus materias y alumnos
    listaCarreras = cargarCarreras()
    print(" ")
    # muestro los nombres y las notas,
    mostrarCarreras(listaCarreras)