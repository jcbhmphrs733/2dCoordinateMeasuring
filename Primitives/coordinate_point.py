from Primitives.circle import *
from Primitives.line import *

class Coor:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
    
    def distance(self, obj):
        if isinstance(obj, AbstractCircle):
            return m.sqrt((self.x - obj.origin.x)**2 + (self.y - obj.origin.y)**2)
        elif isinstance(obj, Coor):
            return m.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)


