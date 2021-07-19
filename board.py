class Board:

    def __init__(self):
        self.opened_locations = set([1, 2, 3, 4, 5])
        # self.discard_pile = set()

    def get_opened_location(self):
        return self.opened_locations

    def open_location(self, number):
        self.opened_locations.add(number)


