from locator import locator
from npc import NPC
from world import World
import numpy as np
import pytest

@pytest.fixture(autouse=True)
def setup():
    world = World()
    locator.provide_world(world)

# Symbols used by tests to describe a scenario
# . = Origin
# p = Player
# > = Agent
# _ = Sight Radius (10 units)
# | = Sight Radius (30 units)

#  ___ 
# |   |
# >  p|
# |___|
# .    
def test_find_player():
    world = locator.get_world()
    world.player.position = np.array([30, 60])
    npc = NPC("NPC", np.array([0, 60]), np.array([1, 0]), 30)
    world.add_entity(npc)
    world.update()
    assert npc.can_see_player() == True

#  ___    
# |   |   
# |   <  p
# |___|   
# .       
def test_search_fail():
    world = locator.get_world()
    world.player.position = np.array([70, 60])
    npc = NPC("NPC", np.array([40, 60]), np.array([-1, 0]), 30)
    world.add_entity(npc)
    world.update()
    assert npc.can_see_player() == False
