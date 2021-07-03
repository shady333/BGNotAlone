class Player:

    def __init__(self):
        self.selected_location = None
        self.available_locations = [1, 2, 3, 4, 5]

    def set_location(self, location_number):
        self.selected_location = location_number
        self.available_locations.remove(location_number)

    def resist(self):
        pass

    def give_up(self):
        pass

    def get_available_locations(self):
        return self.available_locations