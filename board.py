class Board:

    def __init__(self):
        self.opened_locations = [1, 2, 3, 4 , 5]
        self.discard_pile = []

    def dicard_card(self, number):
        self.discard_pile.append(number)

    def open_location(self, number):
        self.opened_locations.append(number)