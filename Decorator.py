#Decorator (patron de diseño)

def decorator(func): 
    def sistema(self, message): 
        print ("Hello:")
        func(self, message) 
    return sistema

class Pc():
    pass
class Version(Pc):
    def ver():
        pass
class System(Pc):
    def info():
        pass
#--------------------------------------------------#
class Windows(System): 
    def __init__(self, name):  
        self.name = name 

    def ver(self):
        pass
    @decorator 
    def inicio(self, message):
        self.message = message 
        print(message)
        print("Dime lo que necesites.")
#--------------------------------------------------#
class Ios(System):
    def __init__(self, name):
        self.name = name 

    def ver(self):
        pass
    @decorator 
    def start(self, message): 
        self.message = message 
        print(message) 
        print("En que puedo ayudarte.") 
        
usuario = Windows('Usuario') 
usuario.inicio('Hola soy cortana')

usuario2 = Ios('Usuario') 
usuario2.start('Hola soy Siri')
