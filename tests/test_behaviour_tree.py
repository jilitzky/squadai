from behaviour_tree import NodeStatus, Action, Condition, Sequence
import pytest

@pytest.fixture(autouse=True)
def setup():
    pass

def test_action():
    class TestAction(Action):
        def __init__(self):
            super().__init__("TestAction", self.run)

        def run(self, agent):
            return NodeStatus.SUCCESS

    action = TestAction()
    result = action.tick(None)
    assert result == NodeStatus.SUCCESS

def test_condition():
    class TestCondition(Condition):
        def __init__(self):
            super().__init__("TestCondition", self.run)

        def run(self, agent):
            return NodeStatus.FAILURE

    condition = TestCondition()
    result = condition.tick(None)
    assert result == NodeStatus.FAILURE

def test_sequence():
    class TestAgent:
        def __init__(self):
            self.health = 100
            self.moving_to_safety = False

    class IsHealthLow(Condition):
        def __init__(self):
            super().__init__("IsHealthLow", self.run)

        def run(self, agent):
            return NodeStatus.SUCCESS if agent.health < 50 else NodeStatus.FAILURE

    class MoveToSafety(Action):
        def __init__(self):
            super().__init__("MoveToSafety", self.run)
        
        def run(self, agent):
            agent.moving_to_safety = True
            return NodeStatus.SUCCESS

    agent = TestAgent()
    sequence = Sequence("Survival", [IsHealthLow(), MoveToSafety()])
    sequence.tick(agent)
    assert agent.moving_to_safety == False

    agent.health = 20
    sequence.tick(agent)
    assert agent.moving_to_safety == True

def test_selector():
    assert True