from blackboard import Blackboard
from entity import Entity
import behaviour_tree as bt
import keys
import numpy as np

class NPC(Entity):
    def __init__(self, name: str, position: np.array, orientation: np.array, sight_range: float, behaviour: bt.Node):
        super().__init__(name, position, orientation)
        self.sight_range = sight_range
        self.behaviour = behaviour
        self.blackboard = Blackboard()

    def update(self):
        self.behaviour.tick(self)

    def knows_player_position(self):
        value, _ = self.blackboard.get(keys.PLAYER_POS, expiry=0)
        return value is not None
