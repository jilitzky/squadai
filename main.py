from blackboard import Blackboard
from agent import Agent
import constants

def run_simulation():
    # 1. Setup
    shared_brain = Blackboard()
    alpha = Agent("Alpha", shared_brain)
    bravo = Agent("Bravo", shared_brain)

    # 2. Step 1: No info
    alpha.update()

    # 3. Step 2: Spotting
    shared_brain.set(constants.KEY_PLAYER_POS, (10, 50))
    alpha.update()
    bravo.update()

if __name__ == "__main__":
    run_simulation()
