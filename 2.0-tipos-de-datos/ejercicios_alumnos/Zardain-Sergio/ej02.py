# -*- coding: utf-8 -*-
#!/usr/local/bin/python3.5

'''
Se requiere ingresar por pantalla notas de alumnos y sus respectivos nombres.
Los nombres deberán contener minimamente 5 caracteres y su nota será entre 0 y 10.
Es necesario calcular el promedio de los alumnos.
'''

if __name__ == '__main__':
    diccionarioAlumnos = {}
    while(True):
        # valido los caracteres del nombre
        while(True):
            nombreAlumno = input("Ingrese nombre del alumno: ")
            if len(nombreAlumno) < 5:
                print("El nombre debera contener 5 caracteres como minimo.")
            else:
                break
        # valido la longitud de la nota
        while(True):
            notaAlumno = float(input("Ingrese la nota del alumno: "))
            if (notaAlumno >= 0 and notaAlumno <= 10) == False:
                print("La nota debe estar entre 0 y 10.")
            else:
                break
        # asigno el alumno al diccionario
        diccionarioAlumnos[nombreAlumno] = notaAlumno
        # pregunto si desea continuar
        print(" ")
        rta = input("Desea cargar mas alumnos? (y/n)")
        print(" ")
        if rta != "y":
            print(" ")
            break
    # muestro los nombres y las notas, luego calculo el promedio
    promedio = 0
    contador = 0
    for elementos,valor in diccionarioAlumnos.items():
        print "Nombre: " + elementos
        print "Nota: " + str(valor)
        promedio += valor
        contador += 1
    promedio /= contador
    print(" ")
    print("Promedio: " + str(promedio))
