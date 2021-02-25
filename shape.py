import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def compareArea(self, otherObj):
        return self.area() / otherObj.area()
    
    def comparePerimeter(self, otherObj):
        return self.perimeter() / otherObj.perimeter()


class Circle(Shape):
    def __init__(self, radius, x, y):
        self.radius
        Shape.__init__(self, x, y)
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def drawCircle(self, fig):
        ax = fig.gca()
        p = patches.Circle((self.x, self.y), self.radius)
        ax.add_patch(p)
    
    
class Rectangle(Shape):
    def __init__(self, length, breadth, x, y):
        self.length = length
        self.breadth = breadth
        Shape.__init__(self, x, y)
        
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return (2 * self.length) + (2 * self.breadth)
    
    def drawRectangle(self, fig):
        ax = fig.gca()
        p = patches.Rectangle((self.x, self.y), self.breadth, self.length)
        ax.add_patch(p)
    

class Square(Rectangle):
    def __init__(self, length, x, y):
        self.width = length
        self.breadth = length
        Rectangle.__init__(self, x, y)
        
        

# main

r = Rectangle(10,5, 0, 0)
print(r.area())
print(r.perimeter())

fig = plt.figure()

plt.ylim(-50, 50)
plt.xlim(-50, 50)

r.drawRectangle(fig)
plt.show()