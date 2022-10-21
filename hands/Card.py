

class Card:

    def __init__(self, name, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = name

    def __repr__(self):
        "return a string representing the card"
        return str(self.name) + " of " + self.suit
