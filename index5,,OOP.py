# Object = A "bundle" of related attributes (variables) and
#            methods (functions) e.g phone,cup,book
#            You need a 'class' to create many Objects

# class = a type of blueprint used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")


car1 = Car("BMW", 2025, "grey", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()


# class variables = Shared among all instances of a class
#                    Allow you to share data among all objects created
#                   from that class.

# Instance Variables = Vars declared  inside the constructor
# Class Variables = Vars defined outside the constructor.

class Student:
    class_year = 2022
    num_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Spongebob", 40)
student2 = Student("Patrick", 32)

print(student1.name)
print(student2.age)
print(Student.class_year)  # we are accessing the variable (class year) from the class because
# it is a class variable

print(student1.num_of_students)  # we are accessing the variable using student1 object which


# will work but will be hard to tell if its a class var or an instance var...its bad code practice and shouldn`t be implemented.


# Inheritance = Allows a class to inherit attributes and methods
#               from another class
#               It helps with code reusability and extensibility

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("WOOF")


class Cat(Animal):
    def speak(self):
        print("MEOW")


class Mouse(Animal):
    def speak(self):
        print("SQUEEK")


dog = Dog("Scooby")
cat = Cat("Garfied")
mouse = Mouse("Mousey")

print(dog.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()

dog.speak()
cat.speak()
mouse.speak()
