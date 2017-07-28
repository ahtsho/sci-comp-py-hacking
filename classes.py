__author__ = 'Ahadu Tsegaye Abebe - 28/07/17'

#Excercises

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __repr__(self):
        return "[{},{}]".format(self.x,self.y)

    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)

    def __sub__(self, other):
        return Point(self.x-other.x,self.y-other.y)

    def __mul__(self, other):
        if isinstance(self,Point) and isinstance(other,Point):
            return Point(self.x*other.x,self.y*other.y)
        else:
            print "_mul_: self={},other={}".format(self,other)
            return Point(self.x*other,self.y*other)

    def __rmul__(self, other):
        print "_rmul_: self={},other={}".format(self,other)
        return Point(self.x*other,self.y*other)

    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False

    def verticalReflect(self, axis):



testpt = Point(3.1,-12.5)
print testpt

A=Point(1,2)
B=Point(3,4)
print A+B, A-B

print A*B
print 3*A
print B*5
print A==B

y=2.5
P=Point(1,2)
Q = P.verticalReflect(y)