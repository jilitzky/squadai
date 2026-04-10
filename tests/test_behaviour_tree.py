from behaviour_tree import NodeStatus, Node
import pytest

@pytest.fixture(autouse=True)
def setup():
    pass

def test_action_node():
    class SuccessNode(Node):
        def __init__(self):
            super().__init__("Success Node")

        def tick(self, agent):
            return NodeStatus.SUCCESS

    node = SuccessNode()
    result = node.tick(None)
    assert result == NodeStatus.SUCCESS
