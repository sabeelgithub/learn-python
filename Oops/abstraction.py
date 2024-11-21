
########################### ABSTRACTION ##############################
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self,lenght,height):
        self.length = lenght
        self.hieght = height
    
    def area(self):
        return print(f"Area of Rectangle is : {self.length * self.hieght}")
    
    def perimeter(self):
        return print(f"Perimeter of Rectangle is : {2 * self.length * self.hieght}")
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__()

    def area(self):
        return print(f"Area of Circle is : {3.14 * self.radius * self.radius}")
    
    def perimeter(self):
        return print(f"Perimeter of Circle is : {2 * 3.14 * self.radius}")
    
    

r = Rectangle(2,2)
r.area()
r.perimeter()

c = Circle(4)
c.area()
c.perimeter()
c.test()

########################### END ABSTRACTION ##############################