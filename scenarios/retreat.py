from blackboard import Blackboard
from agent import Agent
import constants

NAME = "Retreat"

def run():
    bb = Blackboard()
    alpha = Agent("Alpha", bb, health=100)
    bravo = Agent("Bravo", bb, health=20) 
    bb.set(constants.KEY_PLAYER_POS, (10, 50))
    alpha.update()
    bravo.update()
