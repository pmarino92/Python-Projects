from abc import ABC


class Shape(ABC): #abstract class
    def calculate_area(self):
        pass

class Rectangle(Shape):
    length = 5
    breadth = 3
    def calculate_area(self):
        return self.length * self.breadth


class Circle(Shape):
    radius = 4
    def calculate_area(self):
        return 3.14 * self.radius * self.radius


rec = Rectangle() #object created for the class 'Rectangle'
cir = Circle() #object created for the class 'Circle'
print("Area of a rectangle:", rec.calculate_area())
print("Area of a circle:", cir.calculate_area())
