import behaviour_tree as bt
import pytest

@pytest.fixture(autouse=True)
def setup():
    pass

def test_action():
    class TestAction(bt.Action):
        def __init__(self):
            super().__init__("TestAction", self.run)

        def run(self, agent):
            return bt.NodeStatus.SUCCESS

    action = TestAction()
    result = action.tick(None)
    assert result == bt.NodeStatus.SUCCESS

def test_condition():
    class TestCondition(bt.Condition):
        def __init__(self):
            super().__init__("TestCondition", self.run)

        def run(self, agent):
            return bt.NodeStatus.FAILURE

    condition = TestCondition()
    result = condition.tick(None)
    assert result == bt.NodeStatus.FAILURE

def test_sequence():
    class TestAgent:
        def __init__(self):
            self.health = 100
            self.moving_to_safety = False

    class IsHealthLow(bt.Condition):
        def __init__(self):
            super().__init__("IsHealthLow", self.run)

        def run(self, agent):
            return bt.NodeStatus.SUCCESS if agent.health < 50 else bt.NodeStatus.FAILURE

    class MoveToSafety(bt.Action):
        def __init__(self):
            super().__init__("MoveToSafety", self.run)
        
        def run(self, agent):
            agent.moving_to_safety = True
            return bt.NodeStatus.SUCCESS

    agent = TestAgent()
    sequence = bt.Sequence("Survival", [IsHealthLow(), MoveToSafety()])
    sequence.tick(agent)
    assert agent.moving_to_safety == False

    agent.health = 20
    sequence.tick(agent)
    assert agent.moving_to_safety == True

def test_selector():
    assert True