from blackboard import Blackboard
from locator import locator
from world import World
import keys
import numpy as np

def test_get():
    locator.provide_world(World())
    bb = Blackboard()
    bb.set(keys.PLAYER_POS, np.array([0, 0]))
    value, _ = bb.get(keys.PLAYER_POS)
    assert value is not None

def test_get_not_found():
    locator.provide_world(World())
    bb = Blackboard()
    value, _ = bb.get(keys.PLAYER_POS)
    assert value is None

def test_get_confidence():
    world = World()
    locator.provide_world(world)
    bb = Blackboard()
    bb.set(keys.PLAYER_POS, np.array([0, 0]))
    value, confidence = bb.get(keys.PLAYER_POS, expiry=2)
    assert value is not None
    assert confidence == 1.0
    
    locator.get_world().update()
    value, confidence = bb.get(keys.PLAYER_POS, expiry=2)
    assert value is not None
    assert np.isclose(confidence, 0.5)

    locator.get_world().update()
    value, confidence = bb.get(keys.PLAYER_POS, expiry=2)
    assert value is not None
    assert confidence == 0.0
