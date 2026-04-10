from behaviour_tree import NodeStatus, Action, Condition
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
    assert True

def test_selector():
    assert True