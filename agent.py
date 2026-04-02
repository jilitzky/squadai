from blackboard import Blackboard
from simulation import sim
import keys
import math

class Agent:
    # TODO: Should the agent register itself with the sim for ticking?
    def __init__(self, position, orientation, sight_range):
        self.position = position
        self.orientation = orientation
        self.sight_range = sight_range
        self.blackboard = Blackboard()

    def can_see_player(self):
        value, _ = self.blackboard.get(keys.PLAYER_POS, expiry=1)
        return value != None

    # TODO: Should this be done as part of a tick()?
    def search_for_player(self):
        player_pos = sim.player_pos
        # TODO: Is there a vector class I can use to avoid using tuples for position and orientation?
        to_player = (player_pos[0] - self.position[0], player_pos[1] - self.position[1])
        dot = self.dot_product(self.orientation, to_player)
        if (dot >= 0):
            distance = math.dist(self.position, player_pos)
            if distance <= self.sight_range:
                self.blackboard.set(keys.PLAYER_POS, player_pos)

    # TODO: Use NumPy instead
    def dot_product(self, a, b):
        return (a[0] * b[0]) + (a[1] + b[1])