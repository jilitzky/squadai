from vmath import Vector2

class Simulation:
    def __init__(self):
        self.ticks = 0
        self.agents = []
        self.player_pos = Vector2(0, 0)

    def tick(self):
        self.ticks += 1
        for agent in self.agents:
            agent.tick()

    def add_agent(self, agent):
        self.agents.append(agent)

    def move_player(self, position):
        self.player_pos = position

sim = Simulation()
