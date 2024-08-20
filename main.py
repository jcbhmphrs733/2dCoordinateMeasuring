from Formulas.intersection import *
from Primitives.circle import *

# Main code logic
if __name__ == "__main__":
    a = Coor(-4,3)
    b = Coor(3,4)
    c = Coor(4,-3)

    # a = Coor(float(a.split(',')[0]),float(a.split(',')[1]))
    # b = Coor(float(b.split(',')[0]),float(b.split(',')[1]))
    # c = Coor(float(c.split(',')[0]),float(c.split(',')[1]))

    myCircle = CPC(a,b,c)
    myCircle.print_stats()

    
# def generate_cpc(count):
#     for i in count:
#         a = input("a:")
#         b = input("b:")
#         c = input("c:")

#         a = Coor(float(a.split(',')[0]),float(a.split(',')[1]))
#         b = Coor(float(b.split(',')[0]),float(b.split(',')[1]))
#         c = Coor(float(c.split(',')[0]),float(c.split(',')[1]))