from simulation import sim
from typing import Any, Tuple

class Blackboard:
    def __init__(self):
        self.data = {}
        self.timestamps = {}

    def set(self, key: str, value):
        self.data[key] = value
        self.timestamps[key] = sim.ticks

    def get(self, key: str, default=None, expiry: int = None) -> Tuple[Any, float]:
        if key not in self.data:
            return default, 0.0
        
        if expiry is None:
            return self.data[key], 1.0

        age = sim.ticks - self.timestamps[key]
        
        if expiry == 0:
            if age == 0:
                return self.data[key], 1.0
            else:
                return default, 0.0

        confidence = max(1.0 - (age / expiry), 0.0)
        return self.data[key], confidence
