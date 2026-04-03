from agent import Agent
from simulation import sim
import vmath as v

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
    agent = Agent(v.vec2(0, 60), v.vec2(1, 0), 30)
    sim.move_player(v.vec2(30, 60))
    agent.tick() # TODO: Replace with sim.tick()
    assert agent.can_see_player() == True

#  ___    
# |   |   
# |   <  p
# |___|   
# .       
def test_search_fail():
    agent = Agent(v.vec2(40, 60), v.vec2(-1, 0), 30)
    sim.move_player(v.vec2(70, 60))
    agent.tick() # TODO: Replace with sim.tick()
    assert agent.can_see_player() == False
