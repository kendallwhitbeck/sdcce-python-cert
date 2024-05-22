class Person:
    # These VARIABLES will be shared by all instances of the class
    HC_BROWN = "brown"  # "constant" variable for brown hair color (HC)
    HC_BLACK = "black"  # "constant" variable for black hair color (HC)

    def __init__(self, name, age, possessive):  # NOTE: don't use the name and age as parameters yet, too advanced
        self.name = name  # NOTE: use 'name' as a parameter after learning more
        self.age = age  # NOTE: use 'age' as a parameter after learning more
        self.possessive = possessive

    # Dynamic method when called, will increase the person's age by 1 year.
    def birthday(self):
        self.age += 1

    # Static method is a function inside of an object, but doesn't use the self reference.
    def poops(self):  # Static method that everyone does
        print(f"{self.name} 💩")
