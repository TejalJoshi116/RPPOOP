#!/usr/bin/env python
# coding: utf-8

# In[1]:


#speak() and eat() methods in the Animal class use compile-time polymorphism. 


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    def eat(self):
        pass


class Sheep(Animal):
    def speak(self):
        return "Baa!"

    def eat(self):
        return "Grass"


class Tiger(Animal):
    def speak(self):
        return "Roar!"

    def eat(self):
        return "Meat"


class Bird(Animal):
    def speak(self):
        return "Chirp!"

    def eat(self):
        return "Seeds"


animals = [Sheep("Shaun"), Tiger("Raja"), Bird("Tweety")]

while True:
    print("1 - Speak")
    print("2 - Eat")
    print("0 - Quit")
    option = int(input("Enter option: "))

    if option == 1:
        for animal in animals:
            print(animal.name, "says", animal.speak())
    elif option == 2:
        for animal in animals:
            print(animal.name, "eats", animal.eat())
    elif option == 0:
        break
    else:
        print("Invalid option. Please try again.")


# In[ ]:





# In[ ]:




