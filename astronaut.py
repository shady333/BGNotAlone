from PlayerGeneral import PlayerGeneral


class Astronaut(PlayerGeneral):

    def __init__(self):
        PlayerGeneral.__init__(self)
        self.selected_location = None
        self.available_locations = {1, 2, 3, 4, 5}
        self.will = 5

    def set_location(self, location_number):
        self.selected_location = location_number
        self.available_locations.remove(location_number)

    def resist(self):
        pass

    def give_up(self, cards_to_add):
        self.available_locations.update(cards_to_add)
        sorted(self.available_locations)

    def get_available_locations(self):
        if len(self.available_locations) > 0:
            return self.available_locations
        else:
            return 'NONE'

    def add_location(self, number):
        self.available_locations.add(number)