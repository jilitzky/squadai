from enum import Enum

class NodeStatus(Enum):
    SUCCESS = 1
    FAILURE = 2
    RUNNING = 3

class Node:
    def __init__(self, name="Node"):
        self.name = name

    def tick(self, agent):
        raise NotImplementedError("Every node must implement its own tick method.")

class CompositeNode(Node):
    def __init__(self, name="Composite", children=None):
        super().__init__(name)
        self.children = children if children else []

    def add_child(self, child):
        self.children.append(child)

class Selector(CompositeNode):
    def tick(self, agent):
        for child in self.children:
            status = child.tick(agent)

            # Stop if a child is already running or has succeeded.
            if (status != NodeStatus.FAILURE):
                return status
        
        # Every child failed.
        return NodeStatus.FAILURE
    
class Sequence(CompositeNode):
    def tick(self, agent):
        for child in self.children:
            status = child.tick(agent)

            # Stop if a node is still working or has failed.
            if status != NodeStatus.SUCCESS:
                return status
            
        # Every child succeeded!
        return NodeStatus.SUCCESS
