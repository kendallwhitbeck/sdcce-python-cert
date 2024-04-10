class sum_vals_class():
    """
    Sum up values.
    """
    # This is the constructor, it must be the first method in the class definition.
    def __init__(self, a, b):
        # self.a = a  # what does this do?
        # self.b = b
        print("In __init__() method.")
        print(f"a={a}; b={b}.")

    def sum_vals(self, a, b):
        return a + b

def main():
    print("\nRunning main()\n")
    x = 1
    y = 2

    # my_sum = sum_vals_class.sum_vals(x, y)
    # print(f"{x} + {y} = {my_sum}")

    my_sum_vals_class = sum_vals_class(x, y)
    print(my_sum_vals_class)
    print(type(my_sum_vals_class))
    print(f"{x} + {y} = {my_sum_vals_class.sum_vals(x, y)}")

main()