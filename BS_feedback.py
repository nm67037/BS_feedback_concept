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

#I understand how the Card and Deck classes work to create a standard deck of 52 cards.

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_cards(self, card_indices):
        """Plays cards based on the indices provided."""
        selected_cards = [self.hand[i] for i in sorted(card_indices, reverse=True)]
        for index in sorted(card_indices, reverse=True):
            del self.hand[index]
        return selected_cards

    def add_cards(self, cards):
        """Adds cards to the player's hand."""
        self.hand.extend(cards)

    def has_card(self, rank, suit=None):
        """Check if the player has a specific card by rank and optionally suit."""
        return any(card.rank == rank and (suit is None or card.suit == suit) for card in self.hand)

    def __repr__(self):
        return f"{self.name}: {len(self.hand)} cards"

class BSGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.pile = []  # Cards currently in the pile
        self.players = [Player("Human"), Player("AI")]
        self.current_rank = None  # Rank being played this round
        self.starting_player_index = None

    def start_game(self):
        # Deal all cards between the two players
        hands = [self.deck.cards[:26], self.deck.cards[26:]]
        for player, hand in zip(self.players, hands):
            player.hand = hand

        # Determine the starting player based on who has the Ace of Spades
        for i, player in enumerate(self.players):
            if player.has_card("A", "Spades"):
                self.starting_player_index = i
                break

        print(f"{self.players[self.starting_player_index].name} has the Ace of Spades and will start the game.")

    def play_turn(self, player):
        print(f"{player.name}'s turn. Current rank: {self.current_rank if self.current_rank != None else 'Choose a rank to start.'}")

        if player.name == "Human":
            self.human_turn(player)
        else:
            self.ai_turn(player)

    def human_turn(self, player):
        print(f"Your hand: {list(enumerate(player.hand))}")
        print(f"The rank being played this round is: {self.current_rank}")

        # Human chooses cards to play
        card_indices = input(f"Select the indices of cards to play (comma-separated): ")
        try:
            card_indices = list(map(int, card_indices.split(',')))
            played_cards = player.play_cards(card_indices)

            # Human claims to play cards of the current rank
            print(f"You claim to play {len(played_cards)} card(s) as {self.current_rank}")

            # Add the played cards to the pile
            self.pile.extend(played_cards)
            print(f"You placed {len(played_cards)} card(s) in the pile.")

        except (ValueError, IndexError):
            print("Invalid indices. Turn skipped.")


    def ai_turn(self, player):
        print("AI is thinking...")

        if self.current_rank is None:
            self.current_rank = random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])
            print(f"AI chose to start with rank: {self.current_rank}")

        # Simple AI: play all cards of the current rank, or bluff with random cards
        matching_cards = [i for i, card in enumerate(player.hand) if card.rank == self.current_rank]
        if matching_cards:
            played_cards = player.play_cards(matching_cards)
        else:
            played_cards = player.play_cards([random.randint(0, len(player.hand) - 1)])

        self.pile.extend(played_cards)
        print(f"AI played: {played_cards}")

    def play_game(self):
        self.start_game()
        current_player_index = self.starting_player_index

        while True:
            current_player = self.players[current_player_index]
            self.play_turn(current_player)

            # Check for pass or BS logic here (to be implemented)

            current_player_index = (current_player_index + 1) % len(self.players)

if __name__ == "__main__":
    game = BSGame()
    game.play_game()
