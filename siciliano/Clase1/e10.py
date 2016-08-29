#SUPER HARD, vale 10 puntos para Griffindor: Escribir un piedra, papel o tijera de 1 ronda.
#Lo hice al mejor de 3 :P
import random
machine = 0
user = 0
while (not machine == 2) and (not user == 2):
    eleccionUser = input("elija piedra (PI), papel (PA), tijera (TI")
    helpRandom = random.randrange(3)
    if helpRandom == 0:
        eleccionMachine = "PI"
        if eleccionUser == "PA":
            user += 1
        elif eleccionUser == "TI":
            machine += 1
    elif helpRandom == 1:
        eleccionMachine = "PA"
        if eleccionUser == "TI":
            user += 1
        elif eleccionUser == "PI":
            machine += 1
    else:
        eleccionMachine = "TI"
        if eleccionUser == "PI":
            user += 1
        elif eleccionUser == "PA":
            machine += 1
    print("La compu eligio", eleccionMachine)
if user == 2:
    print("Ganaste!")
else:
    print("Perdiste :/")