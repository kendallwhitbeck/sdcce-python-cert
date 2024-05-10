# try_except_file_permission.py

import os

try:
    with open("data/shape.txt", mode="w+") as fp:
        fp.write("Hello, World, 1000")
        a_string = fp.read()
        fp.seek(0)  # move the file pointer back to the beginning of the file
except PermissionError as e:
    print(f"you encountered a PermissionError: {e}")
except FileNotFoundError as e:
    print(f"fnfe {e}")
except Exception as e:
    print(f"e {e}")
else:
    print("No error")
finally:
    print("Always executed. Cleanup")
    # fp.close()  # close the file not needed when using 'with open()'
