# """
# multiple Inheritance = Inherit from more than one parent class
#                             C(A,B)
# Multilevel Inheritance = Inherit from a parent which inherits from another parent
#                              C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("nimon")

rabbit.flee()
hawk.sleep()
fish.eat()


# Super = Function used in a child class to call methods from a
#           parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f" It is {self.color} and {'filled' if self.filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):  # Method Overiding
        print(f"Thea Area is {3.14 * self.radius * self.radius}")
        super().describe()  # Extending functionality of the parent class ...


class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):  # Method Overiding
        print(f"Thea Area is {self.width * self.width}")
        super().describe()  # Extending functionality of the parent class


class Triangle(Shape):
    def __init__(self, color, filled, height, width):
        super().__init__(color, filled)
        self.height = height
        self.width = width

    def describe(self):  # Method Overiding
        print(f"Thea Area is {self.width * self.height}")
        super().describe()  # Extending functionality of the parent class


circle = Circle("red", True, 5)
square = Square("blue", False, 6)
triangle = Triangle("green", False, 8, 9)

print(circle.color)
print(circle.filled)
print(circle.radius)

print(square.color)
print(square.filled)
print(square.width)

print(triangle.color)
print(triangle.filled)
print(triangle.height)

circle.describe()
square.describe()
triangle.describe()

# Polymorphism = Greek word that means to "have many forms or faces"
#               Poly = Many
#               Morphi = Form
# TWO WAYS TO ACHIEVE POLYMORPHISM
#   1.  Inheritance = An object could be treated of the same type as a parent class
#   2. "Duck Typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod
from crypt import methods


class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Method Overiding
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):  # Method Overiding
        return self.side * self.side


class Triangle(Shape):
    def __init__(self, base, height, ):
        self.base = base
        self.height = height

    def area(self):  # Method Overiding
        return self.base * self.height * 0.5


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)  # has overridden the constructor declared in base class(Shape)
        self.topping = topping


shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza(8, 9)]

for shape in shapes:
    print(f"{shape.area()}cm^2")


# "Duck Typing" = Another way to achieve polymorphism besides Inheritance:
#             Objects must have minimum necessary attributes or methods
#              If it looks like a duck, It must be a duck

class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


class Car:
    def speak(self):
        print("Honk!")

    alive = False


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(f"{animal.alive}")


# Static Methods = A method that belong to a class rather than any object from that class                  (instance)
#                   (instance)
# Instance methods = Best for operations on instances of the class (objects)
# Static Methods = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name}={self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


employee1 = Employee("John", "Manager")
employee2 = Employee("Jack", "Cashier")
employee3 = Employee("Joe", "Janitor")

print(Employee.is_valid_position("Doctor"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())


# Class Methods = Allows Operations to the class Itself
#               Take (cls) as the first parameter, which represents the class itself.

class Student:
    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    # This is an instance method
    def get_info(self):
        return f"{self.name} is {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students is: {cls.count}"


student1 = Student("John", 99)
student2 = Student("Jack", 99)
student3 = Student("Joe", 99)

print(Student.get_count())


# Magic methods = Dunder methods (double underscore) __init__,__str__,__eq__
#               They are automatically called by many of pythons built-in operations.
#               They allow developers to define or customize the behaviour of objects.

class Book:
    def __init__(self, author, title, num_of_pages):
        self.author = author
        self.title = title
        self.num_of_pages = num_of_pages

    def __str__(self):
        return f"{self.author} {self.title} "

    def __eq__(self, other):
        return self.author == other.author and self.title == other.title

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_of_pages":
            return self.num_of_pages
        else:
            return f"Key '{key}' was not found in Book"


book1 = Book("John", "Python", 5)
book2 = Book("Jack", "Python", 5)
book3 = Book("Joe", "Python", 5)

print(book1 == book2)

print(book3["author"])
print(book2["title"])
print(book1["num_of_pages"])


# @property = Decorator is used to define a method as a property (It can be accessed like an attribute)
#           Benefit: Add additional logic when read , write,delete attributes
#             Gives you better ,setter and deleter method

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return f"{self._width}"

    @property
    def height(self):
        return f"{self._height}"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be gretaer than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be gretaer than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width was deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height was deleted")


rectangle = Rectangle(2, 4)

rectangle.width = 6
rectangle.height = 8

del rectangle.width
del rectangle.height


# the setter methods above have allowed us to add logic

# """
# Decorator = A function that extends the behaviour of another function
#                 without modifying the base function.
# Pass the base function as an argument to the decorator

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        func(*args, **kwargs)

    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)

    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} icecream")


get_ice_cream("vanilla")

# exception = An event that interupts the flow of a program
#             (ZeroDivisionError,TypeError,ValueError)
#             1.try 2.except 3. finally

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide 1 by zero idiot!!")
except ValueError:
    print("Please enter a number!")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cleanup here")
