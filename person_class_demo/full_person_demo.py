# class_playground.py
# Demonstrate classes using shapes.

# Single Variable
age = 10

# Multiple variable
info = (age, "Kendall")
# print(info)

# Classes allow us to store data and functions within one variable.
class Person:
    # These VARIABLES will be shared by all instances of the class
    HC_BROWN = "brown"  # "constant" variable for brown hair color (HC)
    HC_BLACK = "black"  # "constant" variable for black hair color (HC)

    def __init__(self, name, age):  # NOTE: don't use the name and age as parameters yet, too advanced
        self.name = name  # NOTE: use 'name' as a parameter after learning more
        self.age = age  # NOTE: use 'age' as a parameter after learning more

    # Dynamic method when called, will increase the person's age by 1 year.
    def birthday(self):
        self.age += 1

    # Static method is a function inside of an object, but doesn't use the self reference.
    def poops():  # Static method that everyone does
        print("💩")

# main code
def main():
     # Call static variable
    print(f"Call static variable: Person.HC_BROWN = {Person.HC_BROWN}")

    # Creates an object with type 'Person'; in other words, creates an instance of the 'Person' class called 'kendall'
    kendall = Person("Kendall", 27)

    # Access and print member variables. Member variable is a variable within a class.
    print(f"kendall.name = {kendall.name}")
    print(f"kendall.age = {kendall.age}")
    print(f"kendall.HC_BROWN = {kendall.HC_BROWN}")
        # print(Person.age)  # AttributeError: type object 'Person' has no attribute 'age'

    # Call static method
    Person.poops()
    # Calling static method from instance of a class will error:
        # kendall.poops()  # TypeError: Person.poops() takes 0 positional arguments but 1 was given

    # Call dynamic method: birthday(self)
    kendall.birthday()
    print(f"after birthday, kendall.age = {kendall.age}")
    # Cannot call dynamic method using the class, must be an instance:
        # Person.birthday()  # TypeError: Person.birthday() missing 1 required positional argument: 'self'

main()