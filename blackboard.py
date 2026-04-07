from typing import Any, Tuple

class Blackboard:
    def __init__(self):
        self.data = {}
        self.timestamps = {}

    def set(self, key: str, value, world):
        self.data[key] = value
        self.timestamps[key] = world.frames

    def get(self, key: str, world, default=None, expiry: int = None) -> Tuple[Any, float]:
        if key not in self.data:
            return default, 0.0
        
        if expiry is None:
            return self.data[key], 1.0

        age = world.frames - self.timestamps[key]
        if expiry == 0:
            return (self.data[key], 1.0) if age == 0 else (default, 0.0)

        confidence = max(1.0 - (age / expiry), 0.0)
        return self.data[key], confidence
