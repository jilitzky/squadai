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
            return default, 0.0
        
        if expiry is None:
            return self.data[key], 1.0

        age = sim.ticks - self.timestamps[key]
        if age >= expiry:
            return default, 0.0

        confidence = (expiry - age) / expiry
        return self.data[key], confidence
