from blackboard import Blackboard
from simulation import Simulation
import keys
import math

def test_get():
    sim = Simulation()
    bb = Blackboard()
    bb.set(keys.PLAYER_POS, sim.player_pos, sim.ticks)
    value, _ = bb.get(keys.PLAYER_POS, sim.ticks)
    assert value is not None

def test_get_not_found():
    sim = Simulation()
    bb = Blackboard()
    value, _ = bb.get(keys.PLAYER_POS, sim.ticks)
    assert value is None

def test_get_confidence():
    sim = Simulation()
    bb = Blackboard()
    bb.set(keys.PLAYER_POS, sim.player_pos, sim.ticks)
    value, confidence = bb.get(keys.PLAYER_POS, sim.ticks, expiry=2)
    assert value is not None
    assert confidence == 1.0
    
    sim.tick()
    value, confidence = bb.get(keys.PLAYER_POS, sim.ticks, expiry=2)
    assert value is not None
    assert math.isclose(confidence, 0.5)

    sim.tick()
    value, confidence = bb.get(keys.PLAYER_POS, sim.ticks, expiry=2)
    assert value is not None
    assert confidence == 0.0
