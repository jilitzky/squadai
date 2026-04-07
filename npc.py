from blackboard import Blackboard
from entity import Entity
from locator import locator
import keys
import numpy as np

class NPC(Entity):
    def __init__(self, name: str, position: np.array, orientation: np.array, sight_range: float):
        super().__init__(name, position, orientation)
        self.sight_range = sight_range
        self.blackboard = Blackboard()

    def update(self):
        player_pos = locator.get_world().player.position
        to_player = player_pos - self.position
        to_player_dir = to_player / np.linalg.norm(to_player)
        dot = np.dot(to_player_dir, self.orientation)
        if (dot >= 0):
            distance = np.linalg.norm(to_player)
            if distance <= self.sight_range:
                self.blackboard.set(keys.PLAYER_POS, player_pos)

    def can_see_player(self):
        value, _ = self.blackboard.get(keys.PLAYER_POS, expiry=1)
        return value is not None
