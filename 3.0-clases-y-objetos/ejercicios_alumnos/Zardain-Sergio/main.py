# -*- coding: utf-8 -*-
class MiClase:

	@staticmethod
	def method():
		print(range(10))
		
def main():
	for x in range(10):
		print(x)

if __name__ == "__main__":
	main()
	MiClase.method()
# Que pasa si lo ponemos  "MiClase" debajo del main e intentamos correr
#¿Cómo podemos resolverlo?
