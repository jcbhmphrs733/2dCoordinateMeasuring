from Primitives.coordinate_point import *
from Formulas.intersection import *
from Primitives.line import *
import math as m


class CPC:
    def __init__(self, a: Coor, b: Coor, c: Coor):

        ab = LineSegment(a, b)
        bc = LineSegment(b, c)

        ab_perp = SinglePointLine(ab.mp, ab.perp_m)
        bc_perp = SinglePointLine(bc.mp, bc.perp_m)

        self.origin = Intersection(ab_perp, bc_perp)
        self.radius = m.sqrt((self.origin.x - a.x)**2 + (self.origin.y - a.y)**2)
        
        
    def print_stats(self):
        print(f'Orgin:({round(self.origin.x, 3)},{round(self.origin.y, 3)})\nRadius: {round(self.radius, 3)}')

class SPC:
    def __init__(self, origin: Coor, radius: float):
        pass


