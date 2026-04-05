from vmath import Vector2

class Simulation:
    def __init__(self):
        self.ticks = 0
        self.player_pos = Vector2(0, 0)

    def tick(self):
        self.ticks += 1

    def move_player(self, position: Vector2):
        self.player_pos = position

sim = Simulation()
