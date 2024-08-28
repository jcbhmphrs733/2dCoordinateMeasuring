from Formulas.intersection import *
from Primitives.circle import *
from Primitives.coordinate_point import *
from Primitives.line import *

class Distance():
 
    def __init__(self, *args):

        self.dX = None
        self.dY = None

        if isinstance(args[0], Coor) and isinstance(args[1], Coor):
            # Constructing distance between two Coor.
            self.dist = self._point_to_point(args[0], args[1])
        elif isinstance(args[0], AbstractCircle) and isinstance(args[1], AbstractCircle):
            # Constructing distance between two circles.
            # Find out if user wants center, min, or max dist
            # Center to center dist
            self.dist = self._point_to_point(args[0].origin, args[1].origin)
        elif isinstance(args[0], AbstractLine) and isinstance(args[1], Coor) or isinstance(args[0], Coor) and isinstance(args[1], AbstractLine):
            # Constructing distance between line and point.
            if isinstance(args[0], Coor):
                _coor = args[0]
                _line = args[1]
            else: 
                _coor = args[1]
                _line = args[0]
            self.dist = self._point_to_line(_coor, _line)        
        else:
            raise ValueError("Unexpected types provided for parameters.")

    def _point_to_point(self, a: Coor, b: Coor):

        # Distance between two coor
        return m.sqrt((b.x - a.x)**2 + (b.y - a.y)**2)

    def _point_to_line(self,a: Coor, line1: AbstractLine):
        
        # Distance from point to line along normal path
        normal_intersect = LineIntersect(line1, SinglePointLine(a, line1.perp_m))
        return self._point_to_point(a, normal_intersect)