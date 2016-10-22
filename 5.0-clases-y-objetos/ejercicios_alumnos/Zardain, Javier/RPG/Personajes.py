'''
Created on 12/9/2016

@author: javier_zardain
'''
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252


class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.atributos = {"Fuerza":1,"Agilidad":1,"Inteligencia":1}
        self.experiencia = 0
        self.vida = 100
        self.velocidadCaminar = 0.5
        self.velocidadCorrer = 0.8 + (0.1 * int(self.atributos["Agilidad"]))
        self.estado = "Sano"
        
    def subirNivel(self):
        print(self.nombre + " a subido de nivel!")
        self.nivel = self.nivel + 1
        print("Nivel actual: " + str(self.nivel))
        for x,v in self.atributos.items():
            v = v + 1
            self.atributos[x] = v
            print(x + ": " + str(v))
        
    def sumarExperiencia(self, experiencia):
        self.experiencia = self.experiencia + experiencia
        if(self.experiencia >= (10 * self.nivel)):
            self.subirNivel()
        
    def restarVida(self, damage):
        self.vida = self.vida - damage
        if(self.vida > 0):
            if(self.vida > 10 ):
                if(self.vida > 30):
                    if(self.vida > 60 and self.vida < 100):
                        self.estado = "Levemente herido"
                    else:
                        self.estado = "Herido"
                else:
                    self.estado = "Malherido"
            else:
                self.estado = "Malherido, estado critico"
        else:
            self.estado = "Muerto"
        print(self.nombre + " Puntos de vida: " + str(self.vida) + " Estado: " + self.estado)
    
    def atacar(self):
        return self.atributos["Fuerza"] * 0.5

class Mago(Personaje):
    def __init__(self, nombre):
        Personaje.__init__(self, nombre)
        self.clase = "Mago"
        self.escudoMagico = False
        
    def atacar(self):
        ataque = self.atributos["Inteligencia"] * 1
        return ataque
    
    def recibirDamage(self, damage):
        if(self.escudoMagico):
            damage = damage - self.atributos["Inteligencia"] * 1
        self.restarVida(damage)
        
class Guerrero(Personaje):
    def __init__(self, nombre):
        Personaje.__init__(self, nombre)
        self.clase = "Guerrero"
        self.escudo = False
        
    def atacar(self):
        return self.atributos["Fuerza"] * 1
    
    def recibirDamage(self, damage):
        if(self.escudo):
            damage = damage - self.atributos["Fuerza"] * 1
        self.restarVida(damage)
        
class Persona(Personaje):
    leCaeLaAfip = True
    
    def __init__(self, nombre):
        Personaje.__init__(self, nombre)
        self.clase = "Persona"
        
    def inicializar(self):
        self.laburo = input("La persona tiene laburo? s/n: ") == "s" 
        self.obraSocial = input("La persona tiene Obra Social? s/n: ") == "s" 
        self.sueldo = int(input("Ingrese el salario: "))
        
    def recibirDamage(self, damage):
        self.restarVida(damage)