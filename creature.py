import random

from PlayerGeneral import PlayerGeneral


class Creature(PlayerGeneral):

    def __init__(self):
        PlayerGeneral.__init__(self)
        self.creature_location = -1
        self.target_location = -1
        self.artemia_location = -1
        self.locations = []

    def set_targets(self, opened_locations, discard_pile):
        self.locations = list(set(opened_locations) - set(discard_pile))
        self.set_creature_location()
        self.set_target_location()
        self.set_artemia_location()

    def set_creature_location(self):
        self.creature_location = random.choice(self.locations)

    def set_target_location(self):
        return

    def set_artemia_location(self):
        return

