import random


from .card import Card
from .suit import Suit
from .rank import Rank

import json


class Deck:
    def __init__(self):
        self._cards = []
        self.build()

    def build(self):
        for value in Rank:
            for suit in Suit:
                self._cards.append(Card(value, suit))

        return self._cards

    def numberOfCards(self):
        return len(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)
        print("shuffled Deck")

    def pick(self):
        if self.numberOfCards() > 1:
            return self._cards.pop(0)

    def dealCards(self):
        return [self.pick() for i in range(5)]

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
