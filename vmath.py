import math

class Vector2:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def dist(self, other):
        return math.sqrt(self.dist_sq(other))
    
    def dist_sq(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return (dx * dx) + (dy * dy)    
