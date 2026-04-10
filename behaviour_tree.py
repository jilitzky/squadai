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
