import numpy as np
import math as m

class Coor:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


class CPC:
    def __init__(self, a, b, c):
        
        # extrapolate ab and bc midpoints using coordinate values
        ab_mp = Coor((a.x + b.x)*0.5, (a.y + b.y)*0.5)
        bc_mp = Coor((b.x + c.x)*0.5, (b.y + c.y)*0.5)
        
        # print(f'ABMP:{ab_mp.x,ab_mp.y}')
        # print(f'BCMP:{bc_mp.x,bc_mp.y}')
        
        # determine perpendicular slopes of ab and bc
        ab_perp_m = -1 / ((a.y - b.y) / (a.x - b.x))
        bc_perp_m = -1 / ((b.y - c.y) / (b.x - c.x))

        # print(f'AB_perp_m:{ab_perp_m}')
        # print(f'BC_perp_m:{bc_perp_m}')

        '''
        # print(f'AB_perp expression: Y - {ab_mp.y} = {ab_perp_m}(X - {ab_mp.x})')
        # print(f'AB_perp expression: Y - {ab_mp.y} = ({ab_perp_m})X - {ab_perp_m * ab_mp.x}')
        # print(f'AB_perp expression: {-ab_mp.y} = ({ab_perp_m})X - {ab_perp_m * ab_mp.x} - Y')
        # print(f'AB_perp expression: - {ab_perp_m * ab_mp.x} + {-ab_mp.y} = ({ab_perp_m})X - Y')
        # print(f'AB_perp expression: {-(ab_perp_m * ab_mp.x) +(-ab_mp.y)} = ({ab_perp_m})X - Y')
        '''

        # establish the 2x2 coefficient matrix and the 2x1 solution matrix 
        coefficients = np.array([[-ab_perp_m, 1], [-bc_perp_m, 1]])
        solution = np.array([ab_mp.y + (-ab_mp.x * ab_perp_m), bc_mp.y + (-bc_mp.x * bc_perp_m )])
        
        print()
        self.origin = Coor(np.dot(np.linalg.inv(coefficients),solution)[0], np.dot(np.linalg.inv(coefficients),solution)[1])
        self.radius = m.sqrt(pow((self.origin.x - a.x),2)+pow((self.origin.y - a.y), 2))
        
    def print_stats(self):
        print(f'Orgin:({round(self.origin.x, 4)},{round(self.origin.y, 4)}), Radius:{round(self.radius, 4)}')

class Measure():
    def __init__(self) -> None:
        pass

def generate_cpc(count):
    for i in count:
        a = input("a:")
        b = input("b:")
        c = input("c:")

        a = Coor(float(a.split(',')[0]),float(a.split(',')[1]))
        b = Coor(float(b.split(',')[0]),float(b.split(',')[1]))
        c = Coor(float(c.split(',')[0]),float(c.split(',')[1]))



# Main code logic
if __name__ == "__main__":
    a = input("a:")
    b = input("b:")
    c = input("c:")

    a = Coor(float(a.split(',')[0]),float(a.split(',')[1]))
    b = Coor(float(b.split(',')[0]),float(b.split(',')[1]))
    c = Coor(float(c.split(',')[0]),float(c.split(',')[1]))

    myCircleOne = CPC(a, b, c)
    myCircleTwo = CPC(a, b, c)
    myCircleThree = CPC(a, b, c)
    myCircleFour = CPC(myCircleOne.origin, myCircleTwo.origin, myCircleThree.origin)
    myCircleFour.print_stats()