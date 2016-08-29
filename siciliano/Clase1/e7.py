#Dado un numero ingresado por el usuario, dar la posibilidad al mismo de: generar su sumatoria o su factorial.
numero = int(input("Ingrese un numero "))
sumatoria = input("Quiere hacer sumatoria? S/N")
if sumatoria == "S":
	contador = 0
	suma = 0
	while contador <= numero:
		suma += contador
		contador += 1
	print(suma)
else:
	factorial = input("Quiere hacer factorial? S/N")
	if factorial == "S":
		contador = numero
		while contador>1:
			contador-=1
			numero = numero * contador
		print(numero)