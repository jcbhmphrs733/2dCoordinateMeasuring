from Primitives.coordinate_point import *
from Formulas.intersection import *
from Primitives.line import *
import math as m

class CPC:
    def __init__(self, a, b, c):

        ab = LineSegment(a, b)
        bc = LineSegment(b, c)

        # print('ab')
        # ab.print_stats()
        # print('ab')
        # bc.print_stats()

        ab_perp = SinglePointLine(ab.mp, ab.perp_m)
        bc_perp = SinglePointLine(bc.mp, bc.perp_m)

        # print()
        # print('ab_perp')
        # ab_perp.print_stats()
        # print('bc_perp')
        # bc_perp.print_stats()

        self.origin = Intersection(ab_perp, bc_perp).intersect
        self.radius = m.sqrt((self.origin.x + a.x) ** 2 + (self.origin.y + a.y) ** 2)
        
        
    def print_stats(self):
        print(f'Orgin:({round(self.origin.x, 4)},{round(self.origin.y, 4)}) \nRadius: {round(self.radius,3)}')

