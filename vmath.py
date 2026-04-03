import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)
    
    def dist_sq(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return (dx * dx) + (dy * dy)

    def dist(self, other):
        return math.sqrt(self.dist_sq(other))
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
