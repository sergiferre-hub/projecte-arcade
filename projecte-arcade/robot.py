import random
from unittest import result

class robot:
    name = "machine"
    game = ["pedra","paper","tisora"]

    def playing (self):
        choice = random.choice (self.game)
        return choice

class moneda:
    name = "moneda"
    game = ["cara","creu"]

    def playing (self):
        choice = random.choice (self.game)
        return choice