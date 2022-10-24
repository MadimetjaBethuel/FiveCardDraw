import unittest


from poker.card import Card
from poker.rank import Rank
from poker.suit import Suit
from poker.deck import Deck
from poker.scores import Scores


class CardTest(unittest.TestCase):

    def test_card_suit_null(self):
        self.assertRaises(ValueError, lambda: Card(Rank.TWO, None))

    def test_card_rank_null(self):
        self.assertRaises(ValueError, lambda: Card(None, Suit.CLUBS))

    def test_card_two_of_clubs(self):
        card = Card(Rank.TWO, Suit.CLUBS)
        self.assertEqual("two of clubs", str(card))

    def test_card_ace_of_clubs(self):
        card = Card(Rank.ACE, Suit.CLUBS)
        self.assertEqual("ace of clubs", str(card))

    def test_king_of_hearts(self):
        card = Card(Rank.KING, Suit.HEARTS)
        self.assertEqual("king of hearts", str(card))


class DeckTest(unittest.TestCase):

    def test_deck_size(self):
        deck = Deck()
        self.assertEqual(52, deck.numberOfCards())

    def test_deck_draw_hand(self):
        deck = Deck()
        cards = deck.dealCards()
        self.assertEqual(5, len(cards))
        self.assertEqual(47, deck.numberOfCards())


class HandTest(unittest.TestCase):

    def test_number_of_cards(self):
        deck = Deck()
        hand = Scores(deck.dealCards())
        self.assertEqual(5, hand.numberOfCards())

    def test_four_of_a_kind(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.NINE, Suit.DIAMONDS),
            Card(Rank.NINE, Suit.SPADES),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        hand = Scores(cards)
        self.assertTrue(True == hand.fourOfKind())
        self.assertFalse(False == hand.fourOfKind())

    def test_full_house(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.NINE, Suit.DIAMONDS),
            Card(Rank.TEN, Suit.SPADES),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        hand = Scores(cards)
        self.assertTrue(True == hand.fullHouse())
        self.assertFalse(False == hand.fullHouse())

    def test_flush(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.THREE, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.TEN, Suit.CLUBS),
        ]

        hand = Scores(cards)
        self.assertTrue(True == hand.flush())
        self.assertFalse(False == hand.flush())

    def test_straight(self):
        cards = [
            Card(Rank.QUEEN, Suit.SPADES),
            Card(Rank.JACK, Suit.DIAMONDS),
            Card(Rank.TEN, Suit.CLUBS),
            Card(Rank.NINE, Suit.SPADES),
            Card(Rank.EIGHT, Suit.HEARTS),
        ]
        hand = Scores(cards)
        self.assertTrue(True == hand.straight())
        self.assertFalse(False == hand.straight())

    def test_straight_flush(self):
        cards = [
            Card(Rank.EIGHT, Suit.CLUBS),
            Card(Rank.SEVEN, Suit.CLUBS),
            Card(Rank.SIX, Suit.CLUBS),
            Card(Rank.FIVE, Suit.CLUBS),
            Card(Rank.FOUR, Suit.CLUBS),


        ]
        hand = Scores(cards)
        self.assertTrue(True == hand.straightFlush())
        self.assertFalse(False == hand.straightFlush())

    def test_three_of_a_kind(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.NINE, Suit.DIAMONDS),
            Card(Rank.TEN, Suit.SPADES),
            Card(Rank.TWO, Suit.CLUBS),
        ]

        hand = Scores(cards)
        self.assertTrue(True == hand.threeOfKind())
        self.assertFalse(False == hand.threeOfKind())

    def test_two_pairs(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.TEN, Suit.DIAMONDS),
            Card(Rank.TEN, Suit.SPADES),
            Card(Rank.TWO, Suit.CLUBS),
        ]

        hand = Scores(cards)
        self.assertTrue(True == hand.twoPair())
        self.assertFalse(False == hand.twoPair())

    def test_one_pair(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.TEN, Suit.DIAMONDS),
            Card(Rank.SIX, Suit.SPADES),
            Card(Rank.TWO, Suit.CLUBS),
        ]
        hand = Scores(cards)
        self.assertTrue(True == hand.onePair())
        self.assertFalse(False == hand.onePair())

    def test_high_card(self):
        cards = [
            Card(Rank.THREE, Suit.CLUBS),
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.TEN, Suit.DIAMONDS),
            Card(Rank.SIX, Suit.SPADES),
            Card(Rank.TWO, Suit.CLUBS),
        ]
        hand = Scores(cards)
        self.assertTrue(True == hand.highCard())
        self.assertFalse(False == hand.highCard())


if __name__ == '__main__':
    unittest.main()
