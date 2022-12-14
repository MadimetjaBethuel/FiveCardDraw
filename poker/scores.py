
NUMBER_OF_CARDS = 5


class Scores:

    def __init__(self, cards):

        if not len(cards) == 5 and cards == None:
            raise ValueError("hand cannot be less than 5")
        self.cards = cards
        self.playerCards = [card.rank for card in self.cards]
        self.suits = [card.suit for card in self.cards]

    def numberOfCards(self):
        return len(self.cards)

    def flush(self):

        if len(set(self.suits)) == 1:
            return True
        return False

    def straight(self):
        self.playerCards.sort()
        if not len(set(self.playerCards)) == NUMBER_OF_CARDS:
            return False

        # checking if the cards are consecutive
        elif self.playerCards == list(range(min(self.playerCards), max(self.playerCards) + 1)):
            return True

        else:
            # dealing with aces
            if set(self.playerCards) == set([14, 2, 3, 4, 5]):
                return True
            return False

    def highCard(self):

        if not self.flush() or self.straight() or self.fourOfKind() or self.onePair() or self.straightFlush() or self.threeOfKind() or self.twoPair():
            return True
        else:
            return False

    def pairs(self):
        pairs = []

        for card in self.playerCards:
            if self.playerCards.count(card) == 2 and card not in pairs:
                pairs.append(card)

        return len(pairs)

    def twoPair(self):

        if self.pairs() == 2:
            return True
        else:
            False

    def onePair(self):

        if self.pairs() == 1:
            return True
        else:
            return False

    def threeOfKind(self):
        count = 0

        for card in self.playerCards:
            if self.playerCards.count(card) > count:
                count = self.playerCards.count(card)

        if count == 3 and len(set(self.playerCards)) != 5:
            return True

    def fourOfKind(self):
        for card in self.playerCards:
            if self.playerCards.count(card) == 4:
                return True

    def fullHouse(self):
        twoCards = False
        threeCards = False

        for card in self.playerCards:
            if self.playerCards.count(card) == 2:
                twoCards = True
            elif self.playerCards.count(card) == 3:
                threeCards = True

        if twoCards and threeCards:
            return True

    def straightFlush(self):

        if self.straight() and self.flush():
            return True
        else:
            return False
