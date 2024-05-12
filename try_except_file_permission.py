# try_except_file_permission.py

import os

# Initialize number of errors variables.
num_permissions_errors = num_file_not_found_errors = num_zero_division_errors = num_unexpected_errors = 0

try:
    with open("data/shape.txt", mode="w+") as fp:
        fp.write("Hello, World, 1000")
        a_string = fp.read()
        fp.seek(0)  # move the file pointer back to the beginning of the file
        divide_by_zero = 1 / 0
except PermissionError as e:
    print(f"you encountered a PermissionError by trying to write to a file for which you do not have write permission: {e}")
    num_permissions_errors = 1
except FileNotFoundError as e:
    print(f"you encountered a FileNotFoundError by trying to read a file that does not exist: {e}")
    num_file_not_found_errors = 1
except ZeroDivisionError as e:
    print(f"you encountered a ZeroDivisionError by trying to divide by zero: {e}")
    num_zero_division_errors = 1
    divide_by_zero = 1 / 0.001
    print(f"divide_by_zero = {divide_by_zero}")
except Exception as e:
    print(f"you encountered an unexpected error: {e}")
    num_unexpected_errors = 1
else:
    print("No error")
finally:
    print("Always executed. Cleanup")
    # fp.close()  # close file not needed when using 'with open()'
    print(f"PermissionError was raised {num_permissions_errors} times.")
    print(f"FileNotFoundError was raised {num_file_not_found_errors} times.")
    print(f"ZeroDivisionError was raised {num_zero_division_errors} times.")
    print(f"Unexpected error was raised {num_unexpected_errors} times.")