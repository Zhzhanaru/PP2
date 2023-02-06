# 4. Write the definition of a Point class. Objects 
# from this class should have a

#  a method show to display the coordinates of 
# the point
#  a method move to change these coordinates
#  a method dist that computes the distance between 
# 2 points

#distance: sqrt((x1-x0)^2+(y1-y0)^2)
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self):
        dx = int(input())
        dy = int(input())
        self.x = dx
        self.y = dy
    def dist(self):
        print(math.sqrt(self.x*self.x+self.y*self.y))

x = int(input())
y = int(input())
p = Point(x, y)
p.show()
p.move()
p.show()
p.dist()