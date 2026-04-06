from agent import Agent
from simulation import sim
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
    agent = Agent(np.array([0, 60]), np.array([1, 0]), 30)
    sim.move_player(np.array([30, 60]))
    sim.tick()
    assert agent.can_see_player() == True

#  ___    
# |   |   
# |   <  p
# |___|   
# .       
def test_search_fail():
    agent = Agent(np.array([40, 60]), np.array([-1, 0]), 30)
    sim.move_player(np.array([70, 60]))
    sim.tick()
    assert agent.can_see_player() == False
