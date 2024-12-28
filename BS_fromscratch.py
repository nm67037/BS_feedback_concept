import random
from collections import Counter

class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        #__init__pulled ranks and the suits, __represent__ puts them together in pairs
        return f"{self.rank}{self.suit}"
    
   # def __str__(self):
      #  return self.__represent__()  # Use the same representation for str()

class Deck:
    def __init__(self):
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["H", "D", "C", "S"]

        self.cards = [str(Card(suit, rank)) for suit in self.suits for rank in self.ranks]
            #the for loop creates each card as a string and puts the cards in an array
    def shuffle(self):
        random.shuffle(self.cards)
###########################################################switching from cards to players
class Player: #add properties/actions/attributes of players. Right now, "player" is given a name.
    def __init__(self, name: str, hand: list):
        self.name = name
        self.hand = hand
    
    def __repr__(self):
        return self.name
       # return self.hand

    def __str__(self):
        return f"Player: {self.name}, Hand: {self.hand}"


class human(Player): #subclass for the human player, based on the superlass Player
    def __init__(self):
        name = input("What is your name? ").strip()
        hand = []
        super().__init__(name,hand) #putting name into superclass, then calling that superclass attribute and applying it to subclass
     
class AI(Player):
    def __init__(self):
        name = "Ani"
        hand = [] #initialize as empty hand
        super().__init__(name,hand)

    def determine_mode_rank(self): #make the AI able to determine the mode rank of its hand
        if not self.hand:
            return None #sanity check. If the hand is empty, there is no mode
        
        #pull ranks from cards in hand
        ranks = [card[:-1] for card in self.hand] #card is the index variable, moving through each card in the hand. the [:-1] point to the second to last character, and removes anything past that.

        rank_counts = Counter(ranks) #count occurances of each rank
        mode_rank = rank_counts.most_common(1)[0][0]
        return mode_rank
        

############################################################################

class BSGame:
    def __init__(self):
        self.deck = Deck()
        self.human = human()
        self.AI = AI()
        self.players = [self.human, self.AI]
        self.current_rank = None #should be a string, can convert to integer later if needed (J=11, Q=12, A=1, etc)
        self.current_pile = [] #be careful with the AI knowing about the pile. They can only remember the top play, NOT everything underneath
        self.discard_pile = [] #when all players pass

    def start_game(self):
        print(f"Hello, {self.human.name}. My name is {self.AI.name}. Let's play!")
        self.deck.shuffle()
    
        # Deal half the deck to each player
        mid = len(self.deck.cards) // 2
        self.human.hand = self.deck.cards[:mid]  # Human gets the first half
        self.AI.hand = self.deck.cards[mid:]  # AI gets the second half
        print(f"Below is your deck, {self.human.name}. Don't worry, I can't see it :)" )
        print(self.human.hand)

        for player in self.players:
           #print(f"{player.name}'s hand: {player.hand}")
            if 'AS' in player.hand:
                if player == self.AI:
                  print(f"Look's like I have the Ace of Spades, {self.human.name}. I'll put it down and pick a rank to start the game!")
                  self.current_rank = self.AI.determine_mode_rank()
                else:
                    while True:
                        current_rank_beta = input(f"If you have the Ace of Spades, {player.name}, please put it down and choose the rank to start the game with!").strip()
                        if current_rank_beta in self.deck.ranks: #any rank, not just ones human has
                            self.current_rank = current_rank_beta
                            break #only way to exit the loop
                        else:
                            print("That is not a valid rank, " f"{player.name}. Please choose a valid rank.")
                print(self.current_rank)
                           
game = BSGame()
game.start_game()


