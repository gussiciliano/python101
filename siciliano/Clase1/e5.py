#Escribir un programa que reciba un número entero positivo, devolver la sumatoria de dicho número.
numero = int(input())
contador = 0
sumatoria = 0
while contador <= numero:
    sumatoria += contador
    contador += 1
print(sumatoria)