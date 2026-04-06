import numpy as np

class Simulation:
    def __init__(self):
        self.ticks = 0
        self.agents = []
        self.player_pos = np.array([0, 0])

    def tick(self):
        self.ticks += 1
        for agent in self.agents:
            agent.tick(self.player_pos)

    def add_agent(self, agent):
        self.agents.append(agent)

    def move_player(self, position):
        self.player_pos = position
