import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_hands, num_cards):
        """Deal `num_hands` hands with `num_cards` cards each."""
        hands = [self.cards[i*num_cards:(i+1)*num_cards] for i in range(num_hands)]
        self.cards = self.cards[num_hands*num_cards:]
        return hands

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, rank):
        """Plays a card of the given rank, if available."""
        for card in self.hand:
            if card.rank == rank:
                self.hand.remove(card)
                return card
        return None

    def add_cards(self, cards):
        """Adds cards to the player's hand."""
        self.hand.extend(cards)

    def has_rank(self, rank):
        """Check if the player has a card of the given rank."""
        return any(card.rank == rank for card in self.hand)

    def __repr__(self):
        return f"{self.name}: {len(self.hand)} cards"

class BSGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.pile = []  # Cards currently in the pile
        self.players = [Player("Human"), Player("AI")]
        self.turn_index = 0  # Track whose turn it is
        self.current_rank = '2'  # Initial rank to be played

    def start_game(self):
        # Deal cards
        hands = self.deck.deal(len(self.players), len(self.deck.cards) // len(self.players))
        for player, hand in zip(self.players, hands):
            player.hand = hand

    def play_turn(self):
        current_player = self.players[self.turn_index]
        print(f"{current_player.name}'s turn. Current rank: {self.current_rank}")

        if current_player.name == "Human":
            self.human_turn(current_player)
        else:
            self.ai_turn(current_player)

        # Move to next turn
        self.turn_index = (self.turn_index + 1) % len(self.players)
        self.current_rank = self.next_rank(self.current_rank)

    def human_turn(self, player):
        print(f"Your hand: {player.hand}")
        rank = input(f"Enter the rank you want to play (must be {self.current_rank}): ")
        card = player.play_card(rank)
        if card:
            print(f"You played {card}")
            self.pile.append(card)
        else:
            print(f"You don't have any {rank}. You must bluff or pass!")

    def ai_turn(self, player):
        print("AI is thinking...")
        # Simple AI: play if it has the rank, otherwise bluff
        if player.has_rank(self.current_rank):
            card = player.play_card(self.current_rank)
            print(f"AI played {card}")
            self.pile.append(card)
        else:
            bluff_card = random.choice(player.hand)
            player.hand.remove(bluff_card)
            print(f"AI played {bluff_card}")
            self.pile.append(bluff_card)

    def next_rank(self, rank):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return ranks[(ranks.index(rank) + 1) % len(ranks)]

    def is_bs_called(self):
        # Placeholder for BS logic
        return False

    def check_bs(self, player):
        # Placeholder to handle consequences of calling BS
        pass

if __name__ == "__main__":
    game = BSGame()
    game.start_game()
    print("Starting the game!")

    while True:
        game.play_turn()
        if input("Continue? (y/n): ") == 'n':
            break
