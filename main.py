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

def test_area():

    exmp_parallel_line = ParalellLine(exmp_single_point_line, a)
    exmp_parallel_line.print_stats()

    pass


a = Coor(-2,1)
b = Coor(6,5)
c = Coor(2,-1)

c1 = Coor(3,1)
c2 = Coor(4,2)

exmp_line_seg = LineSegment(a, b)
exmp_single_point_line = SinglePointLine(c2, 1/2)


# exmp_circle = CPC(a,b,c)
# exmp_circle.print_stats()

# print(DistancePTP(c1, b))
# print(DistancePTL(c1, exmp_line_seg))




# Main code logic
if __name__ == "__main__":
    test_area()

    pass

# a = Coor(float(a.split(',')[0]),float(a.split(',')[1]))
# b = Coor(float(b.split(',')[0]),float(b.split(',')[1]))
# c = Coor(float(c.split(',')[0]),float(c.split(',')[1]))