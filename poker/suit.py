from enum import Enum

class Suit(Enum):
    SPADES = 1
    HEARTS = 2
    CLUBS = 3
    DIAMONDS = 4

    def __str__(self):
        return self.name.lower()