from astronaut import Astronaut
from board import Board
from creature import Creature


class GameManager:
    def __init__(self):
        self.board = Board()
        self.astro = Astronaut()
        self.creature = Creature()