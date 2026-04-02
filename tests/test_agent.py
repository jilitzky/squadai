from agent import Agent
from simulation import sim

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
    agent = Agent((0, 60), (1, 0), 30)
    sim.move_player((30, 60))
    agent.search_for_player()
    assert agent.can_see_player()

#  ___    
# |   |   
# |   <  p
# |___|   
# .       
def test_search_fail():
    agent = Agent((40, 60), (-1, 0), 30)
    sim.move_player((70, 60))
    agent.search_for_player()
    assert agent.can_see_player() == False
