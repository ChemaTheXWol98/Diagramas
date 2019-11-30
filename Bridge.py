#Bridge
from abc import ABC

class Games(ABC):
    def typeGame(self):
        pass

class typeGame(ABC):
    def __init__(self, games):
        self.games = games

    def year(self):
        pass
#---<Type of game>-------------------------------#
    
class Retro(typeGame):
    def __init__(self, games):
        super(Retro, self).__init__(games)

    def year(self):
        print("Game selected is type retro: ")
        self.games.typeGame(self)
        
#------------------------------------------------#
        
class New(typeGame):
    def __init__(self, games):
        super(New, self).__init__(games)

    def year(self):
        print("Game selected is type new: ")
        self.games.typeGame(self)
        
#------------------------------------------------#
        
class Nostalgic(typeGame):
    def __init__(self, games):
        super(Nostalgic, self).__init__(games)

    def year(self):
        print("Game selected is type nostalgic: ")
        self.games.typeGame(self)
        
#----- <Game> -----------------------------------#
        
class Megaman(Games):
    def typeGame(self):
        print("Game selected is megaman")

class gears(Games):
    def typeGame(self):
        print("Game selected is gears")

class theLoZelda(Games):
    def typeGame(self):
        print("Game selected is the legend of zelda ocarina of time")

#------------------------------------------------#

def main():
    print("\n♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")

    gamer1 = Retro(Megaman)
    gamer1.year()
    
    print("\n♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")

    gamer2 = New(gears)
    gamer2.year()

    print("\n♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")

    gamer3 = Nostalgic(theLoZelda)
    gamer3.year()

    print("\n♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
    
if __name__ == "__main__":
   main()

