# try_except_M5_quiz.py

import csv

import sys

FILENAME = "names.csv"

def main():

    try:

        names = []

        with open(FILENAME, newline="") as file:

            reader = csv.reader(file)

            for row in readers:

                names.append(row)

    except FileNotFoundError as e:

        print("Could not find " + FILENAME + " file.")

        sys.exit()

    except Exception as e:

        print(type(e), e)

        sys.exit()

    print(names)

if __name__ == "__main__":

    main()


