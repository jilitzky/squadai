from agent import Agent
from simulation import sim
from vmath import Vector2

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
    agent = Agent(Vector2(0, 60), Vector2(1, 0), 30)
    sim.move_player(Vector2(30, 60))
    agent.tick() # TODO: Replace with sim.tick()
    assert agent.can_see_player() == True

#  ___    
# |   |   
# |   <  p
# |___|   
# .       
def test_search_fail():
    agent = Agent(Vector2(40, 60), Vector2(-1, 0), 30)
    sim.move_player(Vector2(70, 60))
    agent.tick() # TODO: Replace with sim.tick()
    assert agent.can_see_player() == False
