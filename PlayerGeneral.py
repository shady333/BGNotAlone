class PlayerGeneral:
    def __init__(self):
        self.score = 0

    def get_score(self):
        return self.score

    def increase_score(self, value=1):
        self.score = self.score + value

