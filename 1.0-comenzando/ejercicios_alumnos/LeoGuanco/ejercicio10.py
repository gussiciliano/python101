import random
print("Piedra, papel o tijeras!")
x = random.randint(0,30)
if x <= 10:
	print("Piedra!")
elif x > 10 and x <= 20:
	print("Papel!")
elif x > 20 and x <= 30:
	print("Tijeras!")