from Primitives.circle import *
import math as m

class DistPTP():
    '''
    Distance point to point
    '''
    def __init__(self, a, b):
        self.dist = m.sqrt(m.pow((a.x + b.x), 2) + m.pow((a.y + b.y), 2))

class DistLTP():
    '''
    Distance line to point
    '''
    def __init__(self, ):
        pass

class DistLTL():
    '''
    Distance line to line
    '''
    def __init__(self, ):
        pass




