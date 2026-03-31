from blackboard import Blackboard

KEY_PLAYER_POS = "player_pos"

def test_get():
    bb = Blackboard()
    bb.set(KEY_PLAYER_POS, (0, 0))
    assert bb.get(KEY_PLAYER_POS) != None

def test_get_not_found():
    bb = Blackboard()
    assert bb.get(KEY_PLAYER_POS) == None

def test_get_expired():
    bb = Blackboard()
    bb.set(KEY_PLAYER_POS, (0, 0))
    assert bb.get(KEY_PLAYER_POS, expiry=0) != None
    bb.tick()
    assert bb.get(KEY_PLAYER_POS, expiry=0) == None