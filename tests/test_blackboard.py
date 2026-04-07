from blackboard import Blackboard
from world import World
import keys
import numpy as np

def test_get():
    world = World()
    bb = Blackboard()
    bb.set(keys.PLAYER_POS, np.array([0, 0]), world)
    value, _ = bb.get(keys.PLAYER_POS, world)
    assert value is not None

def test_get_not_found():
    world = World()
    bb = Blackboard()
    value, _ = bb.get(keys.PLAYER_POS, world)
    assert value is None

def test_get_confidence():
    world = World()
    bb = Blackboard()
    bb.set(keys.PLAYER_POS, np.array([0, 0]), world)
    value, confidence = bb.get(keys.PLAYER_POS, world, expiry=2)
    assert value is not None
    assert confidence == 1.0
    
    world.update()
    value, confidence = bb.get(keys.PLAYER_POS, world, expiry=2)
    assert value is not None
    assert np.isclose(confidence, 0.5)

    world.update()
    value, confidence = bb.get(keys.PLAYER_POS, world, expiry=2)
    assert value is not None
    assert confidence == 0.0
