import math as m
import numpy as np
from Primitives.coordinate_point import *

class LineSegment:
    def __init__(self, p1, p2):

        self.m = (p1.y - p2.y) * m.pow((p1.x - p2.x),-1)
        self.mp = Coor((p1.x + p2.x) * 0.5, (p1.y + p2.y) * 0.5)
        self.perp_m = m.pow(self.m, -1)
        self.coefficient = np.array([-self.m, 1])
        self.solution = (m * p1.x) + p1.y

        pass

class SinglePointLine:
    def __init__(self, p1, m):
        
        self.m = m
        self.perp_m = m.pow(self.m, -1)
        self.coefficient = np.array([-self.m, 1])
        self.solution = (m * p1.x) + p1.y

