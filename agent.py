from blackboard import Blackboard
from simulation import sim
import keys
import numpy as np

class Agent:
    def __init__(self, position: np.array, orientation: np.array, sight_range: float):
        self.position = position
        self.orientation = orientation
        self.sight_range = sight_range
        self.blackboard = Blackboard()
        sim.add_agent(self)

    def tick(self):
        player_pos = sim.player_pos
        to_player = player_pos - self.position
        dot = np.dot(self.orientation, to_player)
        if (dot >= 0):
            distance = np.linalg.norm(player_pos - self.position)
            if distance <= self.sight_range:
                self.blackboard.set(keys.PLAYER_POS, player_pos)

    def can_see_player(self):
        value, _ = self.blackboard.get(keys.PLAYER_POS, expiry=0)
        return value is not None
