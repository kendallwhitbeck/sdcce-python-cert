# -*- coding: utf-8 -*-
"""
 Author: Lydell
 Module 1 Assignment 
"""
class Person:
    def __init__(self):
        pass
    
    def __iter__(self):
        db = {"Harry", "Steve"}
        # Return a name from the db, one name at a time.
        for x in db:
            yield(x)
    
    def __next__(self):
        print("next")
        pass

class Student:
    pass

class Teacher:
    pass

for p in Person():
    print(p)

p = Person()
s = Student()
t = Teacher()
