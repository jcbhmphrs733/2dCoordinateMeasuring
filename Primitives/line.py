import numpy as np
from Primitives.coordinate_point import *
from abc import ABC

class AbstractLine(ABC):

    def __init__(self, args):

        # Define slope of the line
        if isinstance(self, LineSegment):
            if args[0].x == args[1].x: self.m = float('inf') #Vertical line
            else: self.m = (args[0].y - args[1].y) / (args[0].x - args[1].x)
        elif isinstance(self, SinglePointLine):
            self.m = args[1]
        elif isinstance(self, ParallelLine):
            self.m = args[0].m
            
        # Define perpendicular slope
        if self.m == float('inf'): self.perp_m = 0
        else: self.perp_m = -self.m ** -1 if self.m != 0 else float('inf')

        # Define the solution and coefficient matricies
        self.coefficient = np.array([-self.m, 1])
        self.solution = (-self.m * args[0].x) + args[0].y

    def __str__(self):
        return f'm:{self.m}\nm_perp:{self.perp_m}\ncoef:{self.coefficient}\nsolution:{self.solution}'

class LineSegment(AbstractLine):

    def __init__(self, p1: Coor, p2: Coor):

        super().__init__(p1, p2)
        self.mp = Coor((p1.x + p2.x) * 0.5, (p1.y + p2.y) * 0.5)
    
class SinglePointLine(AbstractLine):
    def __init__(self, p1: Coor, _m: float):
        
        super().__init__(p1, _m)
        
"""
Bisector Line class needs work
"""   
class BisectorLine(AbstractLine):
    
    type1 = LineSegment
    type2 = SinglePointLine

    def __new__(cls, self, line1: AbstractLine, line2: AbstractLine):

        if isinstance(line1, self.type1) and isinstance(line2, self.type1):
            # Bisecting two line segments creates another line segment.
            
            return LineSegment()
        
        elif isinstance(line1, self.type2) and isinstance(line2, self.type2):
            # Bisecting two single point lines creates another single point line.
            return SinglePointLine()
        
        elif (isinstance(line1, self.type1) and isinstance(line2, self.type2)) or (isinstance(line1, self.type2) and isinstance(line2, self.type1)):
            # Bisecting a line segment and a single point line creates a single point line.
            return SinglePointLine()
        
        else:
            raise ValueError("Unexpected types provided for parameters.")


    def __init__(self, line):

        if isinstance(line, self.type1):

            # Bisecting line is a line segment.
            if line.p1.x == line.p2.x:
                self.m = float('inf') #Vertical line
            else:
                self.m = (line.p1.y - line.p2.y) / (line.p1.x - line.p2.x)

            self.mp = Coor((line.p1.x + line.p2.x) * 0.5, (line.p1.y + line.p2.y) * 0.5)
        
            if self.m == float('inf'):
                self.perp_m = 0
            else:
                self.perp_m = -self.m ** -1 if self.m != 0 else float('inf')
                
            self.coefficient = np.array([-self.m, 1])
            self.solution = (-self.m * line.p1.x) + line.p1.y
        
        elif isinstance(line, self.type2):
            # Bisecting line is a single point line.
            return SinglePointLine()
        pass

    def __str__(self):
        return f"{self.description} Data: {self.data}"

"""
Closed for construction
"""

class ParallelLine(AbstractLine):
    def __init__(self, line1: AbstractLine, p1: Coor):
        
        super().__init__(line1, p1)