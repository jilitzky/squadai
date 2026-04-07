from player import Player

class World:
    def __init__(self):
        self.player = Player()
        self.entities = []
        self.frames = 0

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self):
        self.frames += 1
        for entity in self.entities:
            entity.update()
