"""
Demonstrate usage of the Person module which contains the Person class.
"""

from Person import Person

def main():
    kendall = Person("Kendall", 27, "his")

    kendall.poops()

    print(f"Kendall's age is {kendall.age}")

    kendall.birthday()
    print(f"After {kendall.possessive} birthday, Kendall's age is now {kendall.age}")

if __name__ == "__main__":
    main()

