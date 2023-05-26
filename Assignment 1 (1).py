#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
        if self.length == self.breadth:
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


def display_menu():
    print("Menu:")
    print("1. Create a Rectangle")
    print("2. Create a Square")
    print("3. Create a Circle")
    print("4. Create a Triangle")
    print("5. Create a Hexagon")
    print("6. Exit")


def get_menu_choice():
    choice = input("Enter your choice (1-6): ")
    return choice


def create_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    rectangle = Rectangle(length, breadth)
    rectangle.print_dimensions()
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")


def create_square():
    side = float(input("Enter the side length of the square: "))
    square = Square(side)
    square.print_dimensions()
    print(f"Area: {square.area()}")
    print(f"Perimeter: {square.perimeter()}")


def create_circle():
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    circle.print_dimensions()
    print(f"Area: {circle.area()}")
    print(f"Perimeter: {circle.perimeter()}")


def create_triangle():
    a = float(input("Enter the length of side A of the triangle: "))
    b = float(input("Enter the length of side B of the triangle: "))
    c = float(input("Enter the length of side C of the triangle: "))
    triangle = Triangle(a, b, c)
    triangle.print_dimensions()
    print(f"Area: {triangle.area()}")
    print(f"Perimeter: {triangle.perimeter()}")


def create_hexagon():
    side = float(input("Enter the length of the hexagon side: "))
    hexagon = Hexagon(side)
    print(f"Area: {hexagon.area()}")
    print(f"Perimeter: {hexagon.perimeter()}")


# Main program
while True:
    display_menu()
    user_choice = get_menu_choice()

    if user_choice == '1':
        create_rectangle()
    elif user_choice == '2':
        create_square()
    elif user_choice == '3':
        create_circle()
    elif user_choice == '4':
        create_triangle()
    elif user_choice == '5':
        create_hexagon()
    elif user_choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")


# In[ ]:




