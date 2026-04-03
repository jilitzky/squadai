import numpy as np

class Simulation:
    def __init__(self):
        self.ticks = 0
        self.player_pos = np.array([0, 0])

    def tick(self):
        self.ticks += 1

    def move_player(self, position):
        self.player_pos = position

sim = Simulation()
