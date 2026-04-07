class Time:
    def __init__(self, world):
        self.world = world

    def elapsed(self):
        return self.world.frames
