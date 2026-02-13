# Classes and objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def greeting(self):
        print(f"Hello, {self.name}!")

person = Person("Zeus", 27)

person.greeting()