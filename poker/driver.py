from .card import Card
from .deck import Deck
from .player import Player
from .scores import Scores

deckOfCards = Deck()
deckOfCards.shuffle()
player = Player(deckOfCards.dealCards())
playerCards = player.playerCards
score = Scores(playerCards)


def playerHand():
    return player.serialize_hand(playerCards)


def checkHand():

    straight = score.straight()
    flush = score.flush()
    highCard = score.highCard()
    onePair = score.onePair()
    twoPair = score.twoPair()
    threeOfKind = score.threeOfKind()
    fourOfKind = score.fourOfKind()
    fullHouse = score.fullHouse()

    if straight and flush and straight == 14:
        return "Royal Flush"

    elif straight and flush:
        return "Straigh Flush"

    elif fourOfKind:
        return "Four of a Kind"

    elif fullHouse:
        return "Full house"

    elif flush:
        return "Flush"

    elif straight:
        return "Straight"

    elif threeOfKind:
        return "Three of a Kind"

    elif twoPair:
        return "2 Pair"
    elif onePair:
        return "1 Pair"
    elif highCard:
        return "High CarCard"
