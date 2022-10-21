import random

from Suit import Suit
from Rank import Rank
from Card import Card


class Deck:

    def __init__(self):
        self._cards = []
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        ranks = {"Two": 2,
                 "Three": 3,
                 "Four": 4,
                 "Five": 5,
                 "Six": 6,
                 "Seven": 7,
                 "Eight": 8,
                 "Nine": 9,
                 "Ten": 10,
                 "Jack": 11,
                 "Queen": 12,
                 "King": 13,
                 "Ace": 14}

        for suit in suits:
            for name in ranks:
                self._cards.append(Card(name, ranks[name], suit))

    def shuffle(self):
        random.shuffle(self._cards)
        print("shuffled Deck")

    def pick(self):
        return self._cards.pop(0)

    def dealCards(self):
        return [self.pick() for i in range(5)]
