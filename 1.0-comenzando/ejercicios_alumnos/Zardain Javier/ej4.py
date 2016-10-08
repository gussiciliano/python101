# Escribir un programa que reciba texto, si es una fruta y es una banana o manzana indica "yummi", si no lo es dice "puajjj"

fruta = raw_input("Ingrese una fruta: ")
fruta = fruta.lower()
if(fruta == "banana" or fruta == "manzana"):
	print("Yummi")
else:
	print("Puajjj")

