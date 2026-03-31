import time

class Blackboard:
    def __init__(self):
        self.data = {}
        self.timestamps = {}
        self.ticks = 0 # TODO: Relocate to simulation

    def set(self, key, value):
        self.data[key] = value
        self.timestamps[key] = self.ticks

    def get(self, key, default=None, expiry=None):
        if key not in self.data:
            return default
        
        age = self.ticks - self.timestamps[key]
        if expiry is not None and age > expiry:
            return default
        
        return self.data[key]

    # TODO: The tick should be done on a simulation object
    def tick(self):
        self.ticks += 1
