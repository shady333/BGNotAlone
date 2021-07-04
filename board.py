class Board:

    def __init__(self):
        self.opened_locations = set([1, 2, 3, 4, 5])
        self.discard_pile = set()

    def discard_card(self, number):
        self.discard_pile.add(number)

    def open_location(self, number):
        self.opened_locations.add(number)

    def clear_discard_pile(self):
        res = self.discard_pile
        self.discard_pile = set()
        return res
