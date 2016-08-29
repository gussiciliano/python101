#Computar el número K ingresado! 4⋅∑(−1)i+12i . Ayudita: la sumatoria va de 0 a K, en este caso i es el elemento del ciclo.
numero = int(input("Ingrese un numero K"))
i = 0
suma = 0
while i <= numero:
    suma += (-1)*i + 12*i
    i+=1
suma = suma*4
print(suma)