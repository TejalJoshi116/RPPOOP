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

#made a list to have animals in the program
animals = [Sheep("Shaun"), Tiger("Raja"), Bird("Tweety")]

while True:
    print("==== Animal Information Menu ====")
    print("1. Display Animal Names")
    print("2. Make Animals Speak")
    print("3. Feed Animals")
    print("0. Quit")

    option = input("Enter option: ")

    if option == "1":
        print("=== Animal Names ===")
        for animal in animals:
            print(animal.name)
        print()

    elif option == "2":
        print("=== Animals Speaking ===")
        for animal in animals:
            print(animal.name, "says", animal.speak())
        print()

    elif option == "3":
        print("=== Feed Animals ===")
        for animal in animals:
            print(animal.name, "eats", animal.eat())
        print()

    elif option == "0":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
        print()
