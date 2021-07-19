class PlayerGeneral:
    def __init__(self):
        self.score = 0
        self.discard_pile = set()

    def get_score(self):
        return self.score

    def increase_score(self, value=1):
        self.score = self.score + value

    def add_card_to_discard_pile(self, number):
        self.discard_pile.add(number)

    def remove_card_from_discard_pile(self, number):
        self.discard_pile.remove(number)

    def get_discard_pile(self):
        return self.discard_pile

    def clear_discard_pile(self):
        res = self.discard_pile
        self.discard_pile = set()
        return res
