import numpy as np
from Primitives.coordinate_point import *

class LineSegment:
    def __init__(self, p1, p2):

        self.m = (p1.y - p2.y) / (p1.x - p2.x)
        self.mp = Coor((p1.x + p2.x) * 0.5, (p1.y + p2.y) * 0.5)
        self.perp_m = -self.m ** -1
        self.coefficient = np.array([-self.m, 1])
        self.solution = (self.m * p1.x) + p1.y
    
    def print_stats(self):
        print(f' m:{self.m}, mp:({self.mp.x, self.mp.y}), m_perp:{self.perp_m}, coef:{self.coefficient}, solution:{self.solution}')


class SinglePointLine:
    def __init__(self, p1, _m):
        
        self.m = _m
        self.perp_m = -self.m ** -1
        self.coefficient = np.array([-self.m, 1])
        self.solution = (self.m * p1.x) + p1.y

    def print_stats(self):
        print(f' m:{self.m}, m_perp:{self.perp_m}, coef:{self.coefficient}, solution:{self.solution}')
    
