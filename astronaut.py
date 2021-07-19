from PlayerGeneral import PlayerGeneral

default_will = 5

class Astronaut(PlayerGeneral):

    def __init__(self):
        PlayerGeneral.__init__(self)
        self.selected_location = None
        self.available_locations = {1, 2, 3, 4, 5}
        self.will = default_will

    def set_location(self, location_number):
        self.selected_location = location_number
        self.available_locations.remove(location_number)

    def remove_will(self, number=1):
        self.will = self.will - number

    def resist(self, will_count):
        self.will = self.will - will_count

    def get_available_will(self):
        return self.will

    def give_up(self, cards_to_add):
        self.available_locations.update(cards_to_add)
        sorted(self.available_locations)
        self.will = default_will

    def get_available_locations(self):
        if len(self.available_locations) > 0:
            return self.available_locations
        else:
            return 'NONE'

    def add_location(self, number):
        self.available_locations.add(number)

    def __str__(self):
        print(f'Locations: {self.available_locations}')
        print(f'Will count: {self.will}')
        print(f'Score: {self.score}')
        return 'astronaut'