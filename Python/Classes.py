# Define a class, which is a sort of blueprint for an object
# Instantiate a class to create an object
# Use attributes and methods to define the properties and behaviors of an object
# Use inheritance to create child classes from a parent class
# Reference a method on a parent class using super()
# Check if an object inherits from another class using isinstance()

# Encapsulation allows you to bundle data (attributes) and behaviors (methods) within a class to create a cohesive unit.

# Inheritance enables the creation of hierarchical relationships between classes, allowing a subclass to inherit attributes and methods from a parent class. This promotes code reuse and reduces duplication.

# Abstraction focuses on hiding implementation details and exposing only the essential functionality of an object

# Polymorphism allows you to treat objects of different types as instances of the same base type, as long as they implement a common interface or behavior. 
class Book:
    def __init__(self):
        self.color = 'red'
        self.pages = 20
        self.author = 'erick juma'
        pass

    def pages(self, page):
        self.page = page
        return self.page

    def getWeight(self):
        self.weight = '300g'
        return self.weight

class storyBook(Book):
    def __init__(self):
        super().__init__
        self.pages = 10
        pass

book = Book()

story = storyBook(book)

print("The book is color: {}".format(book.color))

print("The book has: {} pages".format(book.pages))

print("The book is weighing: {}".format(book.getWeight()))

print(f"Storybook inherits Book class but has: {story.pages} pages")

print(f"Storybook weight: {story.color} pages")
class Book:
    def __init__(self):
        self.color = 'red'
        self.pages = 20
        self.author = 'erick juma'
        pass

    def pages(self, page):
        self.page = page
        return self.page

    def getWeight(self):
        self.weight = '300g'
        return self.weight

class storyBook:
    def __init__(self, Book):
        super().__init__
        self.pages = 10
        pass

book = Book()

story = storyBook(book)

# print("The book is color: {}".format(book.color))

# print("The book has: {} pages".format(book.pages))

# print("The book is weighing: {}".format(book.getWeight()))

# print(f"Storybook inherits Book class but has: {story.pages} pages")

# print(f"Storybook weight: {story.color} pages")

# Dunder methods start with __init__ used to customize class

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
    Dunder methods
    """
    def __repr__(self):
        return f"{self.name} is {self.age} years old"

    """
    For user
    """
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        self.sound = sound
        return f"{self.name} produces {self.sound} sound"

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)
jack = Dog("Jack", 3)
jim = Dog("Jim", 5)
# print(jim.speak('Howl'))

#Inheritance Allows sub classes to extend the methods and properties of super class while also defining their own

class JackRussellTerrier(Dog):
        def speak(self, sound='Arf'):
            return f"{self.name} says {sound}"
            # return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)
print(jack.speak('woof'))
print(type(miles))
print(isinstance(miles, Dog))
print(miles.speak())