import constants

class Agent:
    def __init__(self, name, blackboard):
        self.name = name
        self.bb = blackboard

    def say(self, message):
        print(f"[{self.name}]: {message}")

    def update(self):
        player_pos = self.bb.get(constants.KEY_PLAYER_POS, expiry=constants.EXPIRY_PLAYER_DATA)
        
        if not player_pos:
            self.say("I'm idling, no player spotted.")
            return

        if not self.bb.has_role_filled(constants.ROLE_FLANKER):
            self.bb.claim_role(constants.ROLE_FLANKER, self.name)
            self.say(f"I see the player at {player_pos}. I am FLANKING!")
        else:
            active_roles = self.bb.get(constants.KEY_ACTIVE_ROLES)
            flanker_name = active_roles[constants.ROLE_FLANKER]
            
            if flanker_name == self.name:
                self.say("Moving to flank position...")
            else:
                self.say(f"{flanker_name} is flanking. I will SUPPRESS!")
