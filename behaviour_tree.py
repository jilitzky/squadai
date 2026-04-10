from enum import Enum

class NodeStatus(Enum):
    SUCCESS = 1
    FAILURE = 2
    RUNNING = 3

class Node:
    def __init__(self, name):
        self.name = name

    def tick(self, _):
        raise NotImplementedError("Every node must implement its own tick method.")

class Action(Node):
    def __init__(self, name, action_func):
        super().__init__(name)
        self.action_func = action_func

    def tick(self, agent):
        return self.action_func(agent)
    
class Condition(Node):
    def __init__(self, name, check_func):
        super().__init__(name)
        self.check_func = check_func

    def tick(self, agent):
        return self.check_func(agent)

class CompositeNode(Node):
    def __init__(self, name, children=None):
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
            
        # Every child succeeded.
        return NodeStatus.SUCCESS
