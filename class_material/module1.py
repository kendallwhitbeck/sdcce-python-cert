#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lydell
#
# Created:     20/02/2024
# Copyright:   (c) Lydell 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def load_file(filename, filename1, *args):
    print("filename value is:" + filename)
    print("filename1 value is:" + filename1)

    for argument in args:
        print("args value is:" + argument)

def we_were_called_directly():
    #load_file("file1.csv", "file2.csv", )
    load_file("file1.csv", "file2.csv", "file3.csv", "file4.csv", "file5.csv")
    #load_file(args = {"file3.csv, fileA.csv, fileB.csv"}, filename="file1.csv", filename1="file2.csv")


def some_function():
    print("Within some_function() call")
    pass

# Guard statement.
# Checking whether this module (module1.py) is being called directly, or
# being called as an import statement from another module.
if __name__ == '__main__':
    we_were_called_directly()
else:
    some_function()

