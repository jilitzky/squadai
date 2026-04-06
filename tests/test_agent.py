from agent import Agent
from simulation import Simulation
import numpy as np

# . = Origin
# p = Player
# > = Agent
# _ = Sight Radius (10 units)
# | = Sight Radius (30 units)

#  ___ 
# |   |
# >  p|
# |___|
# .    
def test_find_player():
    sim = Simulation()
    agent = Agent(np.array([0, 60]), np.array([1, 0]), 30)
    sim.add_agent(agent)
    sim.move_player(np.array([30, 60]))
    sim.tick()
    assert agent.can_see_player(sim.ticks) == True

#  ___    
# |   |   
# |   <  p
# |___|   
# .       
def test_search_fail():
    sim = Simulation()
    agent = Agent(np.array([40, 60]), np.array([-1, 0]), 30)
    sim.add_agent(agent)
    sim.move_player(np.array([70, 60]))
    sim.tick()
    assert agent.can_see_player(sim.ticks) == False
