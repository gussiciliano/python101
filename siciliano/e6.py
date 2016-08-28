numero = input()
if(numero%3 == 0):
	numero = numero + numero
elif(numero%5 == 0):
	numero = numero + numero
elif(numero%7 == 0):
	numero = numero + numero
print(numero)