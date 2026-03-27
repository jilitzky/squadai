from blackboard import Blackboard
from agent import Agent
import constants

NAME = "Coordinated Attack"

def run():
    bb = Blackboard()
    alpha = Agent("Alpha", bb)
    bravo = Agent("Bravo", bb)
    bb.set(constants.KEY_PLAYER_POS, (10, 50))
    alpha.update()
    bravo.update()
