#Template method

class Guerrero():
   #Explicacion de lo que hace un guerrero

#-------------------------------------#
    def entrena(self):
        pass
    def pelea(self):
        pass
    def cae(self):
        pass
    def gana():
        pass
    #El guerro se:
    def enfrenta(self):
        self.entrena()
        self.pelea()
        self.cae()
        self.gana()
#-------------------------------------#
#Guerrero de dragon ball
class Goku(Guerrero):
    def entrena(self):
        print("Goku entrena")
    def pelea(self):
        print("Goku pelea")
    def cae(self):
        print("Cae")
    def gana(self):
        print("Se levanta y gana")

#Guerrero de onepice
class Luffy(Guerrero):
    def entrena(self):
        print("Luffy entrena")
    def pelea(self):
        print("Luffy pelea")
    def cae(self):
        print("Cae")
    def gana(self):
        print("Se levanta y gana")

#-------------------------------------#
#Clase Villano
#-------------------------------------#

class Villano():
   #Explicacion de un villano

#-------------------------------------#
    def destruye(self):
        pass
    def pelea(self):
        pass
    def confia(self):
        pass
    def muere():
        pass
    #El villano se:
    def enfrenta(self):
        self.destruye()
        self.pelea()
        self.confia()
        self.muere()
#-------------------------------------#
#Villano de cualquier serie*
class Villano(Villano):
    def destruye(self):
        print("Villano ataca una ciudad")
    def pelea(self):
        print("Pelea con el heroe")
    def confia(self):
        print("Se confia de que gana")
    def muere(self):
        print("Muere")

print("------------------------------------\n")
guerrero1 = Goku()
guerrero1.enfrenta()
print("\n------------------------------------\n")
guerrero2 = Luffy()
guerrero2.enfrenta()
print("\n------------------------------------\n")
villano = Villano()
villano.enfrenta()
print("\n------------------------------------")
