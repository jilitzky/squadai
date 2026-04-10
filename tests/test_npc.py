from locator import locator
from npc import NPC
from world import World
import behaviour_tree as bt
import keys
import numpy as np
import pytest

class CanSeePlayer(bt.Condition):
    def __init__(self):
        super().__init__("CanSeePlayer", self.run)

    def run(self, agent: NPC):
        player_pos = locator.get_world().player.position
        to_player = player_pos - agent.position
        to_player_dir = to_player / np.linalg.norm(to_player)
        dot = np.dot(to_player_dir, agent.orientation)
        if (dot >= 0):
            distance = np.linalg.norm(to_player)
            if distance <= agent.sight_range:
                return bt.NodeStatus.SUCCESS

        return bt.NodeStatus.FAILURE
    
class StorePlayerPosition(bt.Action):
    def __init__(self):
        super().__init__("StorePlayerPosition", self.run)

    def run(self, agent: NPC):
        player_pos = locator.get_world().player.position
        agent.blackboard.set(keys.PLAYER_POS, player_pos)

class FindPlayer(bt.Sequence):
    def __init__(self):
        super().__init__("FindPlayer", [CanSeePlayer(), StorePlayerPosition()])

# Symbols used by tests to describe a scenario
# . = Origin
# p = Player
# > = Agent
# _ = Sight Radius (10 units)
# | = Sight Radius (30 units)

@pytest.fixture(autouse=True)
def setup():
    world = World()
    locator.provide_world(world)

#  ___ 
# |   |
# >  p|
# |___|
# .    
def test_find_player():
    world = locator.get_world()
    world.player.position = np.array([30, 60])
    npc = NPC("NPC", np.array([0, 60]), np.array([1, 0]), 30, FindPlayer())
    world.add_entity(npc)
    world.update()
    assert npc.knows_player_position() == True

#  ___    
# |   |   
# |   <  p
# |___|   
# .       
def test_find_player_fail():
    world = locator.get_world()
    world.player.position = np.array([70, 60])
    npc = NPC("NPC", np.array([40, 60]), np.array([-1, 0]), 30, FindPlayer())
    world.add_entity(npc)
    world.update()
    assert npc.knows_player_position() == False
