import random

class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
    
    def __represent__(self):
        #__init__pulled ranks and the suits, __represent__ puts them together in pairs
        return f"{self.rank}{self.suit}"
    
    def __str__(self):
        return self.__represent__()  # Use the same representation for str()

class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["H", "D", "C", "S"]

        self.cards = [str(Card(suit, rank)) for suit in suits for rank in ranks]
            #the for loop creates each card as a string and puts the cards in an array
    def shuffle(self):
        random.shuffle(self.cards)

class Player: #add properties/actions/attributes of players. Right now, "player" is given a name.
    def __init__(self,name):
        self.name = name
    
    def __represent__(self):
        return self.name

class human(Player): #subclass for the human player, based on the superlass Player
    def __init__(self):
        name = input("What is your name?") #can add .strip() to clear whitespace
        super().__init__(name) #putting name into superclass, then calling that superclass attribute and applying it to subclass

class AI(Player):
    def __init__(self):
        name = "Ani"
        super().__init__(name)

#human = human()
#AI = AI()

#print(AI.name)
#print(human.name)

def start_game():
    Deck = Deck()
    human = human()
    AI = AI()

start_game()