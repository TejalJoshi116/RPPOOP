#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass


class Polygon(Shape):
    def __init__(self, name, sides):
        super().__init__(name)
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)


class Rectangle(Polygon):
    
    def __init__(self, length, breadth):
        super().__init__("Rectangle", [length, breadth, length, breadth])
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def print_dimensions(self):
        print(f"Length: {self.length}")
        print(f"Breadth: {self.breadth}")
        
    def is_square(self):
        if(self.length == self.breadth):
            print("Rectangle is a square.")
        else:
            print("Rectangle is not a square")

    def change_dimensions(self, new_length, new_breadth):
        self.length = new_length
        self.breadth = new_breadth



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def print_dimensions(self):
        print(f"Radius: {self.radius}")
       
    def change_dimensions(self, new_radius):
        self.radius = new_radius
       



class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__("Triangle", [a, b, c])
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def print_dimensions(self):
        print(f"Side A: {self.a}")
        print(f"Side B: {self.b}")
        print(f"Side C: {self.c}")
       
    def change_dimensions(self, new_a, new_b, new_c):
        self.a = new_a
        self.b = new_b
        self.c = new_c
        
        

class Hexagon(Polygon):
    def __init__(self, side):
        super().__init__("Hexagon", [side] * 6)
        self.side = side

    def area(self):
        return ((3 * (3 ** 0.5)) / 2) * self.side ** 2
    
    def perimeter(self):
        return 6 * self.side
        
r = Rectangle(5, 10)
print("Rectangle: Area =", r.area(), " Perimeter =", r.perimeter())

r.change_dimensions(2,5)
r.print_dimensions()

print("Rectangle: Area =", r.area(), " Perimeter =", r.perimeter())

s = Square(7)
print("Square: Area =", s.area(), " Perimeter =", s.perimeter())

c = Circle(3)
print("Circle: Area =", c.area(), " Perimeter =", c.perimeter())

t = Triangle(3, 4, 5)
print("Triangle: Area =", t.area(), " Perimeter =", t.perimeter())

h = Hexagon(6)
print("Hexagon: Area =", h.area(), " Perimeter =", h.perimeter())

