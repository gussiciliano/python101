numero = int(input("Ingrese un numero "))
sumatoria = input("Quiere hacer sumatoria? S/N")
if(sumatoria == "S"):
	numero = numero + numero
	print(numero)
else:
	factorial = input("Quiere hacer factorial? S/N")
	if(factorial == "S"):
		contador = numero
		while(contador>1):
			contador-=1
			numero = numero * contador
		print(numero)