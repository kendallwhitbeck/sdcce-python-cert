# Iterators
my_string = "hello"

# Iterating backwards using negative indexing
for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i])

# Iterating backwards using reversed function
print(reversed(my_string))
for i in reversed(my_string):
    print(i)
    
# Iterate using range
for i in range(20, 100, 10):
    print(i)
    
# using `pass` in a for loop
letter = "Hizthere,zThisziszhowzazpasszstatementzworks!"
for i in letter:
    if i == "mn":
        pass
    elif i == "z":
        print(" ",end="")
    else:
        print(i, end="")
        

