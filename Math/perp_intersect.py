
class PerpIntersect:
    def __init__(self, line1, point1):
        
                
        # establish the 2x2 coefficient matrix and the 2x1 solution matrix 
        coefficients = np.array([[-ab_perp_m, 1], [-bc_perp_m, 1]])
        solution = np.array([ab_mp.y + (-ab_mp.x * ab_perp_m), bc_mp.y + (-bc_mp.x * bc_perp_m )])
        
        print()
        self.intersection = Coor(np.dot(np.linalg.inv(coefficients),solution)[0], np.dot(np.linalg.inv(coefficients),solution)[1])
        