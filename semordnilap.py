"""
Recursive function that reverses the input string that reveals 'palindromes' ('semordnilap' backwards).
"""

def semordnilap(aString,index):
    if index == 0:
        print(f"aString=`{aString}`")
        print(f"len(aString)={len(aString)}")
        print("begin processing palindrome:")
    if index < len(aString):
        # print(aString[index], end="")
        semordnilap(aString, index + 1)
        print(aString[index], end="")

semordnilap("alucard",0)