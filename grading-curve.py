# This application displays a student's score after a 5-point curve

def display_info(fname, lname, score):
    print("Hello, " , fname, " " , Lname)
    print("Your score on this exam is ", score)
    score = score + 5

def main():
    first = input("first name: ")
    last = input("last name: ")
    grade = input("exam score: ")
    display_info(last, first, score)

#if started as the main module, call the main function
if __name__ == "__main__":
    main()
