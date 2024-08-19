import numpy as np
from Primitives.coordinate_point import *
from Formulas.intersection import *
import math as m
from Primitives.line import *


class CPC:
    def __init__(self, a, b, c):

        ab = LineSegment(a, b)
        bc = LineSegment(b, c)

        ab_perp = SinglePointLine(ab.mp, ab.perp_m)
        bc_perp = SinglePointLine(bc.mp, bc.perp_m)

        self.origin = Intersection(ab_perp, bc_perp).intersect
        
        # # extrapolate ab and bc midpoints using coordinate values
        # ab_mp = Coor((a.x + b.x)*0.5, (a.y + b.y)*0.5)
        # bc_mp = Coor((b.x + c.x)*0.5, (b.y + c.y)*0.5)
       
        # # determine perpendicular slopes of ab and bc
        # ab_perp_m = -1 / ((a.y - b.y) / (a.x - b.x))
        # bc_perp_m = -1 / ((b.y - c.y) / (b.x - c.x))

        # # establish the 2x2 coefficient matrix and the 2x1 solution matrix 
        # coefficients = np.array([[-ab_perp_m, 1], [-bc_perp_m, 1]])
        # solution = np.array([ab_mp.y + (-ab_mp.x * ab_perp_m), bc_mp.y + (-bc_mp.x * bc_perp_m )])
        
        # print()
        # self.origin = Coor(np.dot(np.linalg.inv(coefficients),solution)[0], np.dot(np.linalg.inv(coefficients),solution)[1])
        # self.radius = m.sqrt(pow((self.origin.x - a.x),2)+pow((self.origin.y - a.y), 2))
        
    def print_stats(self):
        print(f'Orgin:({round(self.origin.x, 4)},{round(self.origin.y, 4)})')


# def generate_cpc(count):
#     for i in count:
#         a = input("a:")
#         b = input("b:")
#         c = input("c:")

#         a = Coor(float(a.split(',')[0]),float(a.split(',')[1]))
#         b = Coor(float(b.split(',')[0]),float(b.split(',')[1]))
#         c = Coor(float(c.split(',')[0]),float(c.split(',')[1]))