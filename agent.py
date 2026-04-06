from blackboard import Blackboard
import keys
import numpy as np

class Agent:
    def __init__(self, position: np.array, orientation: np.array, sight_range: float):
        self.position = position
        self.orientation = orientation
        self.sight_range = sight_range
        self.blackboard = Blackboard()

    def tick(self, player_pos: np.array, sim_ticks: int):
        to_player = player_pos - self.position
        to_player_dir = to_player / np.linalg.norm(to_player)
        dot = np.dot(self.orientation, to_player_dir)
        if (dot >= 0):
            distance = np.linalg.norm(player_pos - self.position)
            if distance <= self.sight_range:
                self.blackboard.set(keys.PLAYER_POS, player_pos, sim_ticks)

    def can_see_player(self, sim_ticks: int):
        value, _ = self.blackboard.get(keys.PLAYER_POS, sim_ticks, expiry=0)
        return value is not None
