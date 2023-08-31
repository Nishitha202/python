import math
class shape:
    def __init__(self):
        self.area=0
        self.name=""
    def showArea(self):
        print("the area of",self.name,"is",self.area,"units")
class circle(shape):
    def __init__(self,radius):
        self.area = 0
        self.name = "circle"
        self.radius=radius
    def clacArea(self):
        self.area =math.pi*self.radius*self.radius


class Rectangle(shape):
    def __init__(self,length,breadth):
        self.area = 0
        self.name = "Rectangle"
        self.length=length
        self.breadth=breadth

    def clacArea(self):
        self.area =  self.length * self.breadth

class Triangle(shape):
    def __init__(self,base,height):
        self.area = 0
        self.name = "Triangle"
        self.base=base
        self.height=height

    def clacArea(self):
        self.area =  self.base * self.height/2
c1=Circle(2)
c1.clacArea()
c1.showArea()

r1=Rectangle(8,4)
r1.clacArea()
r1.showArea()

T1=Triangle(2,4)
T1.clacArea()
T1.showArea()
