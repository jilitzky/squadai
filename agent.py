import constants

class Agent:
    def __init__(self, name, blackboard, health=100):
        self.name = name
        self.bb = blackboard
        self.health = health

    def say(self, message):
        print(f"[{self.name} (HP:{self.health})]: {message}")

    def update(self):
        # 1. Survival Check
        if self.health < constants.HEALTH_THRESHOLD_RETREAT:
            self.bb.claim_role(constants.ROLE_RETREATING, self.name)
            self.say("I'm too wounded! RETREATING to safety!")
            return

        # 2. Information Gathering
        player_pos = self.bb.get(constants.KEY_PLAYER_POS, expiry=constants.EXPIRY_PLAYER_DATA)
        
        if not player_pos:
            self.say("I'm idling, no player spotted.")
            return

        # 3. Tactical Logic
        if not self.bb.has_role_filled(constants.ROLE_FLANKER):
            self.bb.claim_role(constants.ROLE_FLANKER, self.name)
            self.say(f"Flanking player at {player_pos}!")
        else:
            active_roles = self.bb.get(constants.KEY_ACTIVE_ROLES)
            flanker_name = active_roles[constants.ROLE_FLANKER]
            
            if flanker_name == self.name:
                self.say("Continuing flank maneuver...")
            else:
                self.say(f"Covering {flanker_name}. I am SUPPRESSING!")

