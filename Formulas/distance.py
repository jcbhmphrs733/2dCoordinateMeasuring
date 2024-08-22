from Formulas.intersection import *
from Primitives.circle import *
from Primitives.coordinate_point import *
from Primitives.line import *

class Distance():

    def __new__(cls, obj1, obj2):
        if isinstance(obj1, Coor) and isinstance(obj2, Coor):
            # Constructing distance between two Coor.
            return cls._point_to_point(obj1, obj2)
        
        elif isinstance(obj1, cls.type_circle) and isinstance(obj2, cls.type_circle):
            # Constructing distance between two circles.
            # Find out if user wants center, min, or max dist
            # Center to center dist
            return cls._point_to_point(obj1.origin, obj2.origin)
        
        elif isinstance(obj1, AbstractLine) and isinstance(obj2, Coor):
            # Constructing distance between line and point.
            return cls._point_to_line(obj2, obj1)
        
        elif isinstance(obj1, Coor) and isinstance(obj2, AbstractLine ):
            # Constructing distance between point and line.
            return cls._point_to_line(obj1, obj2)

        else:
            raise ValueError("Unexpected types provided for parameters.")

    def _point_to_point(a: Coor, b: Coor):
        # Distance formula
        return m.sqrt((b.x - a.x)**2 + (b.y - a.y)**2)

    def _point_to_line(self, a: Coor, line1: AbstractLine):
        # Normal distance from point to line
        normal_intersect = LineIntersect(line1, SinglePointLine(a, line1.perp_m))
        return self._point_to_point(a, normal_intersect)