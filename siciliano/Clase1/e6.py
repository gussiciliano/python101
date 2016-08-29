#Modificar el ejercicio anterior generando que únicamente sume números que sean múltiplos de 3, 5 o 7 hasta el número ingresado.
numero = input()
if(numero%3 == 0):
	numero = numero + numero
elif(numero%5 == 0):
	numero = numero + numero
elif(numero%7 == 0):
	numero = numero + numero
print(numero)