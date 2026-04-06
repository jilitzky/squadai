from blackboard import Blackboard
import keys
import numpy as np

class Agent:
    def __init__(self, position: np.array, orientation: np.array, sight_range: float, sim):
        self.position = position
        self.orientation = orientation
        self.sight_range = sight_range
        self.blackboard = Blackboard(sim)

    def tick(self, player_pos: np.array):
        to_player = player_pos - self.position
        to_player_dir = to_player / np.linalg.norm(to_player)
        dot = np.dot(self.orientation, to_player_dir)
        if (dot >= 0):
            distance = np.linalg.norm(player_pos - self.position)
            if distance <= self.sight_range:
                self.blackboard.set(keys.PLAYER_POS, player_pos)

    def can_see_player(self):
        value, _ = self.blackboard.get(keys.PLAYER_POS, expiry=0)
        return value is not None
