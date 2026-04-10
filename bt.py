from abc import ABC, abstractmethod
from enum import Enum

class TaskStatus(Enum):
    WAITING = 1
    STEPPING = 2
    SUCCESS = 3
    FAILURE = 3

class Task(ABC):
    def __init__(self):
        self.status = TaskStatus.WAITING 

    def is_terminated(self):
        return self.status == TaskStatus.SUCCESS or self.status == TaskStatus.FAILURE
    
    @abstractmethod
    def perform_action(self):
        """This method must be implemented by child classes."""
        pass

    def step(self):
        terminated = self.is_terminated()
        if not terminated:
            self.status = self.perform_action()
        return self.status
