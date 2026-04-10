import behaviour_tree as bt
import pytest

class Agent:
    def __init__(self):
        self.health = 100
        self.moving_to_safety = False
        self.player_spotted = False
        self.flanking_player = False

class IsHealthLow(bt.Condition):
    def __init__(self):
        super().__init__("IsHealthLow", self.run)

    def run(self, agent: Agent):
        return bt.NodeStatus.SUCCESS if agent.health < 50 else bt.NodeStatus.FAILURE

class IsPlayerSpotted(bt.Condition):
    def __init__(self):
        super().__init__("IsPlayerSpotted", self.run)

    def run(self, agent: Agent):
        return bt.NodeStatus.SUCCESS if agent.player_spotted else bt.NodeStatus.FAILURE

class MoveToSafety(bt.Action):
    def __init__(self):
        super().__init__("MoveToSafety", self.run)
    
    def run(self, agent: Agent):
        agent.moving_to_safety = True
        return bt.NodeStatus.SUCCESS
    
class FlankPlayer(bt.Action):
    def __init__(self):
        super().__init__("FlankPlayer", self.run)
    
    def run(self, agent: Agent):
        agent.flanking_player = True
        return bt.NodeStatus.SUCCESS

@pytest.fixture(autouse=True)
def setup():
    pass

def test_action():
    class TestAction(bt.Action):
        def __init__(self):
            super().__init__("TestAction", self.run)

        def run(self, _):
            return bt.NodeStatus.SUCCESS

    action = TestAction()
    result = action.tick(None)
    assert result == bt.NodeStatus.SUCCESS

def test_condition():
    class TestCondition(bt.Condition):
        def __init__(self):
            super().__init__("TestCondition", self.run)

        def run(self, _):
            return bt.NodeStatus.FAILURE

    condition = TestCondition()
    result = condition.tick(None)
    assert result == bt.NodeStatus.FAILURE

def test_sequence():
    agent = Agent()
    sequence = bt.Sequence("Sequence", [IsHealthLow(), MoveToSafety()])
    sequence.tick(agent)
    assert agent.moving_to_safety == False

    agent.health = 20
    sequence.tick(agent)
    assert agent.moving_to_safety == True

def test_selector():
    agent = Agent()
    survival = bt.Sequence("Survival", [IsHealthLow(), MoveToSafety()])
    attack = bt.Sequence("Attack", [IsPlayerSpotted(), FlankPlayer()])
    selector = bt.Selector("Selector", [survival, attack])
    selector.tick(agent)
    assert agent.flanking_player == False

    agent.player_spotted = True
    selector.tick(agent)
    assert agent.flanking_player == True
