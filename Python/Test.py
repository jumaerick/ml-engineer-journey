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