class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self, other: "Person"):
        print(
            f"Hello, {other.name}! My name is {self.name} and I'm {self.age}"
        )


def divide(n, m):
    # An exception is raised that we didnt expect
    # We try to return early from a function
    try:
        print("TRY")
        value = n / m
    except ZeroDivisionError:
        print("EXCEPT ZERO_DIVISION_ERROR")
        return 0
    else:
        print("ELSE")
        return value
    finally:
        print("FINALLY")


def main():
    # everything goes right
    # result = divide(6, 2)
    # print(result, end="\n\n")

    # # something goes wrong, but we expected it to
    # result = divide(6, 0)
    # print(result, end="\n\n")

    # # something we didnt expect happens
    # result = divide("6", "2")
    # print(result)
    adam = Person("Adam smith", 25)
    laura = Person("Laura Johnson", 42)

    print(adam)
    print(laura)

    adam.greet(laura)
    laura.greet(adam)
