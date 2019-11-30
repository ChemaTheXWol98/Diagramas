#Decorator (patron de diseño)

def decorator(func): 
    def sistema(self, message): 
        print ("Hello:")
        func(self, message) 
    return sistema

class System():
    pass
#--------------------------------------------------#
class windows(System): 
    def __init__(self, name):  
        self.name = name 
    	
    @decorator 
    def inicio(self, message):
        self.message = message 
        print(message)
        print("Dime lo que necesites.")
#--------------------------------------------------#
class ios(System):
    def __init__(self, name):
        self.name = name 
    	
    @decorator 
    def start(self, message): 
        self.message = message 
        print(message) 
        print("En que puedo ayudarte.") 
        
usuario = windows('Usuario') 
usuario.inicio('Hola soy cortana')

usuario2 = ios('Usuario') 
usuario2.start('Hola soy Siri')
