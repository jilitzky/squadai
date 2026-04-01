from blackboard import Blackboard
from simulation import sim

KEY_PLAYER_POS = "player_pos"

def test_get():
    bb = Blackboard()
    bb.set(KEY_PLAYER_POS, (0, 0))
    value, _ = bb.get(KEY_PLAYER_POS)
    assert value != None

def test_get_not_found():
    bb = Blackboard()
    value, _ = bb.get(KEY_PLAYER_POS)
    assert value == None

def test_get_confidence():
    bb = Blackboard()
    bb.set(KEY_PLAYER_POS, (0, 0))
    value, confidence = bb.get(KEY_PLAYER_POS, expiry=2)
    assert value != None
    assert confidence == 1.0
    
    sim.tick()
    value, confidence = bb.get(KEY_PLAYER_POS, expiry=2)
    assert value != None
    assert confidence == 0.5

    sim.tick()
    value, confidence = bb.get(KEY_PLAYER_POS, expiry=2)
    assert value == None
    assert confidence == 0.0
