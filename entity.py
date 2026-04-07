import numpy as np

class Entity:
    def __init__(self, name: str, position: np.array, orientation: np.array):
        self.name = name
        self.position = position
        self.orientation = orientation
