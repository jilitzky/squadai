from simulation import sim

class Blackboard:
    def __init__(self):
        self.data = {}
        self.timestamps = {}

    def set(self, key, value):
        self.data[key] = value
        self.timestamps[key] = sim.ticks

    def get(self, key, default=None, expiry=None):
        if key not in self.data:
            return default
        
        age = sim.ticks - self.timestamps[key]
        if expiry is not None and age > expiry:
            return default
        
        return self.data[key]
