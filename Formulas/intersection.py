from Primitives.line import * 
from Primitives.coordinate_point import * 
import numpy as np

class Intersection:
    def __new__(cls, line1: AbstractLine, line2: AbstractLine):
    
        # establish the 2x2 coefficient matrix and the 2x1 solution matrix 
        coefficients = np.array([line1.coefficient, line2.coefficient])
        solution = np.array([line1.solution, line2.solution])
        
        product = np.dot(np.linalg.inv(coefficients), solution)

        return Coor(product[0],product[1])
    
    def __init__(self, intersection):

        self.intersection = intersection
        