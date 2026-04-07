from entity import Entity
import numpy as np

class Player(Entity):
    def __init__(self):
        super().__init__("Player", np.array([0, 0]), np.array([1, 0]))

    def update(self):
        pass
