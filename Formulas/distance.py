from Formulas.intersection import *
from Primitives.circle import *


class DistancePTP():
    def __new__(cls, a: Coor, b: Coor):
        return m.sqrt((b.x - a.x)**2 + (b.y - a.y)**2)


class DistancePTL():
    def __new__(cls, a: Coor, line1: AbstractLine):
        normal_intersect = LineIntersect(line1, SinglePointLine(a, line1.perp_m))
        return DistancePTP(a, normal_intersect)


class DistanceLTL():
    def __new__(cls, line1: AbstractLine, line2: AbstractLine):
        
        pass

