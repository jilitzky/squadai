from entity import Entity

class World:
    def __init__(self):
        self.entities = []
        self.frames = 0

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self):
        for entity in self.entities:
            entity.update()

        self.frames += 1
