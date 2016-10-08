aux = 0
num = int(input("Ingrese un numero entero positivo: "))
if num>0:
	for x in range(0,num+1):
		if x%3 == 0:
			aux = aux + x
		elif x%5 == 0:
			aux = aux + x
		elif x%7 == 0:
			aux = aux + x
print (aux)