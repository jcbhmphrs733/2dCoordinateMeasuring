from Primitives.coordinate_point import *
from Formulas.intersection import *
from Primitives.line import *
from abc import ABC
import math as m

class AbstractCircle(ABC):


    def distance(self, end):

        if isinstance(end, Coor):
            return self.origin  
        
        return

    def __str__(self):
        return f"Orgin:({round(self.origin.x, 3)},{round(self.origin.y, 3)})\nRadius: {round(self.radius, 3)}"

class CPC(AbstractCircle): # Circumference point circle
    def __init__(self, a: Coor, b: Coor, c: Coor):

        ab = LineSegment(a, b)
        bc = LineSegment(b, c)

        ab_perp = SinglePointLine(ab.mp, ab.perp_m)
        bc_perp = SinglePointLine(bc.mp, bc.perp_m)

        self.origin = LineIntersect(ab_perp, bc_perp)
        self.radius = m.sqrt((self.origin.x - a.x)**2 + (self.origin.y - a.y)**2)
        
class SPC(AbstractCircle): # Single point circle
    def __init__(self, origin: Coor, radius: float):
        
        self.origin = origin
        self.radius = radius