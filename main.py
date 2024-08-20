from Formulas.intersection import *
from Formulas.distance import *
from Primitives.circle import *

# Main code logic
if __name__ == "__main__":
    a = Coor(-3,4)
    b = Coor(4,3)
    c = Coor(3,-4)

    # a = Coor(float(a.split(',')[0]),float(a.split(',')[1]))
    # b = Coor(float(b.split(',')[0]),float(b.split(',')[1]))
    # c = Coor(float(c.split(',')[0]),float(c.split(',')[1]))

    myCircle = CPC(a,b,c)
    myCircle.print_stats()

    e = Coor(3,7)
    d = Coor(6,-4)

    print()
    my_distance = DistPTP(d, e)
    print(my_distance.dist)
    
# def generate_cpc(count):
#     for i in count:
#         a = input("a:")
#         b = input("b:")
#         c = input("c:")

#         a = Coor(float(a.split(',')[0]),float(a.split(',')[1]))
#         b = Coor(float(b.split(',')[0]),float(b.split(',')[1]))
#         c = Coor(float(c.split(',')[0]),float(c.split(',')[1]))