# person class

class Person:
    def __init__(self):
        self.first_name = "John"
        self.last_name = "Watkins"
        self.csv_filename = ""
        self.csv_file_contents = ""

per = Person()

print(per.first_name, per.last_name)