from world import World

class Locator:
    def get_world(self):
        return self.world
    
    def provide_world(self, world: World):
        self.world = world

locator = Locator()
