from PlayerGeneral import PlayerGeneral


class Astronaut(PlayerGeneral):

    def __init__(self, will_count, start_locations={1, 2, 3, 4, 5}):
        PlayerGeneral.__init__(self)
        self.selected_location = None
        self.available_locations = start_locations
        self.will = will_count
        self.init_will = will_count

    def set_location(self, location_number):
        self.selected_location = location_number
        self.available_locations.remove(location_number)

    def end_of_phase(self):
        self.add_card_to_discard_pile(self.selected_location)
        self.selected_location = None

    def remove_will(self, number=1):
        self.will = self.will - number

    def get_available_will(self):
        return self.will

    def give_up(self, cards_to_add):
        self.available_locations.update(cards_to_add)
        sorted(self.available_locations)
        self.will = self.init_will

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