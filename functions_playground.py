# functions_playground
import os
# os.("cls")

def load_file(file1, file2, *args):
    print("load_file() function")
    print(file1)
    print(file2)
    print(args)
    
def load_file_kwargs(**kwargs):
    print("~~~ load_file_kwargs() function ~~~")
    print("kwargs =", kwargs)
    print("type(kwargs) =", type(kwargs))
    print("kwargs.keys() =", kwargs.keys())
    print("kwargs.values() =", kwargs.values())
    print("kwargs.items() =", kwargs.items())
    for key in kwargs.keys():
        print(key)
    for val in kwargs.values():
        print(val)
    for k,v in kwargs.items():
        print(k,v)
    for k_v_pair_tuple in kwargs.items():
        print(k_v_pair_tuple)

# use *args for loading multiple files
load_file("file2.txt", "file1.txt", "file3.txt", "file4.txt")
# load_file(file1="file1.txt", file2="file2.txt", "file3.txt") # SyntaxError: positional argument follows keyword argument

# use keyword args for loading files
load_file_kwargs(file1="file1.csv", file2="file2.csv", file3="file3.csv", file4="file4.csv") # must assign kwarg var names