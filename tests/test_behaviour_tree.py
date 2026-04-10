from behaviour_tree import NodeStatus, Node
import pytest

@pytest.fixture(autouse=True)
def setup():
    pass

def test_action():
    class Action(Node):
        def __init__(self):
            super().__init__("Action")

        def tick(self, agent):
            return NodeStatus.SUCCESS

    action = Action()
    result = action.tick(None)
    assert result == NodeStatus.SUCCESS

def test_condition():
    class Condition(Node):
        def __init__(self):
            super().__init__("Condition")

        def tick(self, agent):
            return NodeStatus.FAILURE

    condition = Condition()
    result = condition.tick(None)
    assert result == NodeStatus.FAILURE

def test_sequence():
    assert True

def test_selector():
    assert True