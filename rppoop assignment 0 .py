#!/usr/bin/env python
# coding: utf-8

# ASSIGNMENT 0

# In[5]:


#class representing a rectangle 
#operations like area, perimeter, change dimensions, report dimensions 

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(polygon):
    def __init__(self, length, width):
        
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def print_dimensions(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        
    def is_square(self):
        if(self.length == self.width):
            print("Rectangle is a square.")
        else:
            print("Rectangle is not a square")

    def change_dimensions(self, new_length, new_width):
        self.length = new_length
        self.width = new_width


rect = Rectangle(4, 6)

rect.print_dimensions()

print(f"Area: {rect.area()}")

print(f"Perimeter: {rect.perimeter()}")

rect.change_dimensions(5, 7)

rect.print_dimensions()

rect.is_square()

rect.change_dimensions(7, 7)

rect.print_dimensions()

rect.is_square()


# ASSIGNMENT 1

# In[3]:





# assignmnet 1

# In[ ]:





# In[ ]:




