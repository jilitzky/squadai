import time

class Blackboard:
    def __init__(self):
        self.data = {}
        self.timestamps = {}

    def set(self, key, value):
        self.data[key] = value
        self.timestamps[key] = time.time()

    def get(self, key, default=None, expiry=None):
        if key not in self.data:
            return default
        if expiry and (time.time() - self.timestamps[key] > expiry):
            return default
        return self.data[key]

    def has_role_filled(self, role_name):
        from constants import KEY_ACTIVE_ROLES
        return self.get(KEY_ACTIVE_ROLES, {}).get(role_name, False)

    def claim_role(self, role_name, agent_id):
        from constants import KEY_ACTIVE_ROLES
        roles = self.get(KEY_ACTIVE_ROLES, {})
        roles[role_name] = agent_id
        self.set(KEY_ACTIVE_ROLES, roles)
