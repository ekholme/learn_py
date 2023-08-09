# this is mostly adapted from the python manual section on classes
# https://docs.python.org/3/tutorial/classes.html


# define a new class
class MyClass:
    x = 123

    def greet(self):
        return "Hello from MyClass"


x = MyClass()

# see class attributes
x.greet()
x.x


# we can define an __init()__ method to help us create object instances with specific initial states
class MyClass:
    def __init__(self, x):
        self.x = x

    def greet(self):
        return "Hello from MyClass"


y = MyClass(x=1)
y.x


# class variables will be shared by all instances, whereas instance variables will be unique to each instance
class Dog:
    kind = "canine"  # class variable

    def __init__(self, name):
        self.name = name


d = Dog("Nala")
e = Dog("Adi")

d.name
d.kind
e.name


# below might be a way to create a Dog class where each dog has its own set of tricks
class Dog:
    kind = "canine"

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Nala")
d.add_trick("roll over")
d.add_trick("sit")

d.tricks


# classes also support inheritance
class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    kind = "cat"


a = Cat("Fluffy")

a.name
a.kind
