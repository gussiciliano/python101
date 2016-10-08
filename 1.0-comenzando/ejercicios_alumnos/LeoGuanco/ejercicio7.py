aux = 0
num = int(input("Ingrese un numero entero positivo: "))
opc = int(input("1- Sumatoria, 2-Factorial: "))
if opc == 1:
	for x in range(0,num+1):
		aux = aux + x
	print (aux)
elif opc == 2:
	if num == 0:
		print("1")
	elif num > 0:
		aux = 1
		for x in range(1,num+1):
			aux = aux*x
		print (aux)
	elif num < 0:
		print("Se deberia haber ingresado un numero valido")