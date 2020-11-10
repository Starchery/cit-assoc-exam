class Person:
    """ Class variables """

    current_year = 2020

    def __init__(self, name: str, age: int):
        """ Instance variables """
        self.name = name
        self.age = age

    def greet(self, other: "Person"):
        print(
            f"Hello, {other.name}! My name is {self.name} and I'm {self.age}"
        )


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def boss_around(self, other):
        print(f"Get to work, {other.name}!")


class Manager(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

    def boss_around(self, other):
        if isinstance(other, Manager):
            print("Hi pal")
        else:
            super().boss_around(other)


class DataHolder:
    value = 25

    def speak(self):
        print("Hello from DataHolder!")


class Animal:
    def bark(self):
        print("Hello")


class NewData(DataHolder):
    def speak(self):
        """Method overriding"""
        """Polymorphism"""
        print("Hello from NewData!")


class Speaker:
    def speak(self):
        print("This is a speaker")


class DataSpeaker(Animal, Speaker, DataHolder):
    """
    Method Resolution Order
    The leftmost class takes priority over
    the others.
    """

    pass


class DataDog(Animal, DataHolder):
    pass


class A:
    def speak(self):
        print("A")


class B(A):
    def speak(self):
        print("B")


class C(A):
    def speak(self):
        print("C")


class D(C, B):
    """ Method resolution order (MRO) """

    """ __bases__ """

    def speak(self):
        print("D")


class LinkedList:
    def __init__(self):
        pass

    def __len__(self):
        pass


adam = Person("Adam smith", 23)
laura = Person("Laura johnson", 55)
