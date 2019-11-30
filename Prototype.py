#prototype
import copy

class Pokemon():
   pass

class Prototype(Pokemon):
   tipo = None
   nivel = None

   def clonar(self):
      pass
   def obtenerTipo(self):
      return self.tipo
   def obtenerNivel(self):
      return self.nivel

class Pokemon1(Prototype):
   def __init__(self, numero):
      self.tipo = "Pokemon 1"
      self.nivel = numero

   def clonar(self):
      return copy.copy(self)

class Pokemon2(Prototype):
   def __init__(self, numero):
      self.tipo = "Pokemon 2"
      self.nivel = numero

   def clonar(self):
      return copy.copy(self)

class Objetos:
   tipo1Nivel1 = None
   tipo1Nivel2 = None
   tipo2Nivel1 = None
   tipo2Nivel2 = None

   @staticmethod
   def inicializar():
      Objetos.tipo1Nivel1 = Pokemon1(1)
      Objetos.tipo1Nivel2 = Pokemon1(2)
      
      Objetos.tipo2Nivel1 = Pokemon2(1)
      Objetos.tipo2Nivel2 = Pokemon2(2)

   @staticmethod
   def obtenerTipo1Nivel1():
      return Objetos.tipo1Nivel1.clonar()

   @staticmethod
   def obtenerTipo1Nivel2():
      return Objetos.tipo1Nivel2.clonar()

   @staticmethod
   def obtenerTipo2Nivel1():
      return Objetos.tipo2Nivel1.clonar()

   @staticmethod
   def obtenerTipo2Nivel2():
      return Objetos.tipo2Nivel2.clonar()

def main():
   Objetos.inicializar()
   
   instance = Objetos.obtenerTipo1Nivel1()
   print ("%s: %s" % (instance.obtenerTipo(), instance.obtenerNivel()))

   instance = Objetos.obtenerTipo1Nivel2()
   print ("%s: %s" % (instance.obtenerTipo(), instance.obtenerNivel()))

   instance = Objetos.obtenerTipo2Nivel1()
   print ("%s: %s" % (instance.obtenerTipo(), instance.obtenerNivel()))

   instance = Objetos.obtenerTipo2Nivel2()
   print ("%s: %s" % (instance.obtenerTipo(), instance.obtenerNivel()))
   #-------------------------------------------------#

if __name__ == "__main__":
   main()
