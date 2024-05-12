# file_io_playground.py
"""
This is what data/file_io_playground.txt looks like initially:
Index, Temp
0, 72
1, 72
2, 6
3, 55
4, 40
5, 38

This is what I want data/file_io_playground.txt to look like after the program is run:
Hello, World!
Index, Temp
0, 72
1, 72
2, 6
3, 55
4, 40
5, 38
"""

# fileObj = open("data/file_io_playground.txt", mode='r')  # if file does not exist, fails with FileNotFoundError: [Errno 2] No such file or directory: 'file_io_playground.txt'
fileObj = open("data/file_io_playground.txt", mode="a+")  # if file does not exist, creates it. If file exists, overwrites it.

file_data = fileObj.read()

fileObj.seek(0)  # move the file pointer back to the beginning of the file

fileObj.write("Hello, World!\n")
# print(file_data)

# save the file
# fileObj.flush()  # saves the file

# print("\n~~~~~~\n")

fileObj.seek(0)  # move the file pointer back to the beginning of the file, this is required to read the entire file
file_data = fileObj.read()
print(file_data)


# file_data = fileObj.write("Hello, World!")
# print(file_data)

fileObj.close()



