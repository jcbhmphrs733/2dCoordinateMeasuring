from Formulas.intersection import *
from Formulas.distance import *
from Primitives.circle import *
from Primitives.line import *
from Primitives.coordinate_point import *

circles = []
points = []
lines = []


def add_new_object(circles, points, lines):

    pass


# Main code logic
if __name__ == "__main__":




    a = Coor(-2,1)
    b = Coor(6,5)
    c = Coor(2,-1)
    c1 = Coor(3,1)
    c2 = Coor(4,2)
    

    newLine = LineSegment(a, b)
    
    print(DistancePTP(c1, b))
    print(DistancePTL(c, newLine))
    print(DistancePTL(c1, newLine))
    print(DistancePTL(c2, newLine))

    # myCircle = CPC(a,b,c)
    # myCircle.print_stats()

    # a = Coor(float(a.split(',')[0]),float(a.split(',')[1]))
    # b = Coor(float(b.split(',')[0]),float(b.split(',')[1]))
    # c = Coor(float(c.split(',')[0]),float(c.split(',')[1]))
