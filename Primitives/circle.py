from Primitives.coordinate_point import *
from Formulas.intersection import *
from Primitives.line import *


class CPC:
    def __init__(self, a, b, c):

        ab = LineSegment(a, b)
        bc = LineSegment(b, c)

        ab.print_stats()
        bc.print_stats()

        ab_perp = SinglePointLine(ab.mp, ab.perp_m)
        bc_perp = SinglePointLine(bc.mp, bc.perp_m)

        print()
        ab_perp.print_stats()
        bc_perp.print_stats()

        self.origin = Intersection(ab_perp, bc_perp).intersect
        
        
    def print_stats(self):
        print(f'Orgin:({round(self.origin.x, 4)},{round(self.origin.y, 4)})')

