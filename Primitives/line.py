import numpy as np
from Primitives.coordinate_point import *
from abc import ABC

class AbstractLine(ABC):
    def print_stats(self) -> None:
        '''
        Abstract method that must be 
        implemented by subclasses.
        '''

class LineSegment(AbstractLine):
    def __init__(self, p1: Coor, p2: Coor):

        if p1.x == p2.x:
            self.m = float('inf') #Vertical line
        else:
            self.m = (p1.y - p2.y) / (p1.x - p2.x)

        self.mp = Coor((p1.x + p2.x) * 0.5, (p1.y + p2.y) * 0.5)
        
        if self.m == float('inf'):
            self.perp_m = 0
        else:
            self.perp_m = -self.m ** -1 if self.m != 0 else float('inf')
            
        self.coefficient = np.array([-self.m, 1])
        self.solution = (-self.m * p1.x) + p1.y
    
    def print_stats(self):
        print(f' m:{self.m}, mp:({self.mp.x, self.mp.y}), m_perp:{self.perp_m}, coef:{self.coefficient}, solution:{self.solution}')


class SinglePointLine(AbstractLine):
    def __init__(self, p1: Coor, _m: float):
        
        self.m = _m
        self.perp_m = -self.m ** -1
        self.coefficient = np.array([-self.m, 1])
        self.solution = (-self.m * p1.x) + p1.y

    def print_stats(self):
        print(f' m:{self.m}, m_perp:{self.perp_m}, coef:{self.coefficient}, solution:{self.solution}')
    
