from blackboard import Blackboard
from simulation import sim
import keys

class Agent:
    def __init__(self, position, orientation, sight_range):
        self.position = position
        self.orientation = orientation
        self.sight_range = sight_range
        self.blackboard = Blackboard()
        sim.add_agent(self)

    def tick(self):
        player_pos = sim.player_pos
        to_player = player_pos - self.position
        dot = self.orientation.dot(to_player)
        if (dot >= 0):
            distance = self.position.dist(player_pos)
            if distance <= self.sight_range:
                self.blackboard.set(keys.PLAYER_POS, player_pos)

    def can_see_player(self):
        value, _ = self.blackboard.get(keys.PLAYER_POS, expiry=0)
        return value is not None
