

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)

    def serialize(self):
        """Convert card into a JSON string."""
        card_json = "{} of {}".format(self.rank, self.suit)
        return card_json
