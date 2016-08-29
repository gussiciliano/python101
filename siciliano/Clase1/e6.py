#Modificar el ejercicio anterior generando que unicamente sume numeros que sean multiplos de 3, 5 o 7 hasta el número ingresado.
numero = int(input())
contador = 0
sumatoria = 0
if numero%3 == 0 or numero%5 == 0 or numero%7 == 0:
	while contador <= numero:
		sumatoria += contador
		contador += 1
print(sumatoria)