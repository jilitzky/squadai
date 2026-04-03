from blackboard import Blackboard
from simulation import sim
import keys
import math

def test_get():
    bb = Blackboard()
    bb.set(keys.PLAYER_POS, sim.player_pos)
    value, _ = bb.get(keys.PLAYER_POS)
    assert value is not None

def test_get_not_found():
    bb = Blackboard()
    value, _ = bb.get(keys.PLAYER_POS)
    assert value is None

def test_get_confidence():
    bb = Blackboard()
    bb.set(keys.PLAYER_POS, sim.player_pos)
    value, confidence = bb.get(keys.PLAYER_POS, expiry=2)
    assert value is not None
    assert confidence == 1.0
    
    sim.tick()
    value, confidence = bb.get(keys.PLAYER_POS, expiry=2)
    assert value is not None
    assert math.isclose(confidence, 0.5)

    sim.tick()
    value, confidence = bb.get(keys.PLAYER_POS, expiry=2)
    assert value is not None
    assert confidence == 0.0
