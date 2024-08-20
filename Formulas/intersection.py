from Primitives.line import * 
from Primitives.coordinate_point import * 
import numpy as np

class Intersection:
    def __init__(self, line1, line2):
           
        # establish the 2x2 coefficient matrix and the 2x1 solution matrix 
        coefficients = np.array([line1.coefficient, line2.coefficient])
        solution = np.array([line1.solution, line2.solution])
        
        product = np.dot(np.linalg.inv(coefficients), solution)

        self.intersect = Coor(product[0],product[1])
        