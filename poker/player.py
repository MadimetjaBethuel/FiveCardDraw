

class Player:

    def __init__(self, playerCards):
        self.playerCards = playerCards

    def cardCount(self):
        return len(self.cards)

    def serialize(self, cards):
        """Convert card into a JSON string."""
        card_json = "{} of {}".format(self.playerCards)
        return card_json

    @staticmethod
    def serialize_hand(hand):
        """Serialize player's hand of cards into JSON."""
        hand_json = ''
        for card in hand:
            hand_json += '{},'.format(card.serialize())
        hand_json = hand_json[:-1]

        return hand_json.split(",")
