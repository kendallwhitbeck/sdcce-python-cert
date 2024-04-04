# -*- coding: utf-8 -*-
"""
Author: Kendall Whitbeck
Student ID: 5550203278
Assignment: Module 6: Questions: 2-7
Description: This program explores string manipulation in Python.
"""

import os  # os.system('cls'): clear terminal window text in Windows OS

# Mod 6, Question 2
def Mod6_Q2():
    # Input String
    str = 'inet addr:127.0.0.1  Mask:255.0.0.0'
    
    # Find the index of the first colon
    colon_index = str.find(":")
    
    # Extract the portion of the string after the first colon
    inet_addr = str[colon_index + 1:]
    
    # Find the index of the space before "Mask"
    space_index = inet_addr.find(" ")
    
    # Strip characters following the value for inet addr (i.e., Mask and corresponding value)
    inet_addr = inet_addr.rstrip(inet_addr[space_index:])
    
    # Print extracted value of inet addr
    print(f"2. The extracted internet address is: `{inet_addr}`")  # Output: 127.0.0.1

# Mod 6, Question 3
def Mod6_Q3():
    str = \
    '''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0
inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
    '''
    
    # 3a. Use a for loop through a string and the split method to count the number of internet addresses in str 
    count_3a = 0
    # Iterate through each line in string by splitting at each new line ('\n')
    for line in str.split('\n'):
        if "inet addr" in line:  # if the line indicates it contains an internet address, increment count by 1
            count_3a += 1
    # Print the number of internet addresses in str
    print(f"\n3a. Using split method, the string contains {count_3a} internet addresses.")
    
    # 3b. Use the count() method to to count the number of internet addresses in str
    count_3b = str.count("inet addr")
    # Print the number of internet addresses in str
    print(f"3b. Using count method, the string contains {count_3b} internet addresses.")

# Mod 6, Question 4
def add_html_tags(tag, content):
    return f"<{tag}>{content}</{tag}>"

# Mod 6, Question 5 # 
def greet(first_name=None, last_name=None):

    # Skip asking for user input if first name is provided
    if first_name is None:
        first_name = input("What is your first name ? ")

    # Skip asking for user input if last name is provided
    if last_name is None:
        last_name = input("What is your last name ? ")

    # Print the greeting while capitalizing the first and last names. `title()` ensures that multi-word strings get each 1st letter capitalized
    print(f"Hi {first_name.title()} {last_name.title()} , welcome to my python greet application!")

# Mod 6, Question 6
def abbreviate_middle_name(full_name=None):
    print("\nQ6. Abbreviate Middle Name:")
    
    # Check if input was passed by function call or needs to be user input
    if full_name is None:
        full_name = input("Enter your full name: ")

    # Ensure input is a string
    if type(full_name) is not str:
        full_name = str(full_name)
    #     print("full_name was not string")  # debug only
    # else:  # debug only
    #     print("full_name was already string")  # debug only
    
    # Split full_name into constiuent parts at the spaces
    name_parts = full_name.split()
    
    # Check number of names provided
    if len(name_parts) < 3:
        # If no middle name(s) provided, display first and last names
        print(f"ATTENTION: no middle name(s) provided. Full name is: {full_name}")
        return
    else:
        # Loop through full_name while ignoring first name and last name
        for i in range(1, len(name_parts) - 1):
            # Abbreviate middle name(s) 
            name_parts[i] = name_parts[i][0] + '.'     
        # Join the name parts back together    
        abbreviated_name = ' '.join(name_parts)
        print(abbreviated_name)
        return

# Mod 6, Question 7
def query_famous_people(full_name=None):
    
    # Check if input was passed by function call or needs to be user input
    if full_name is None:
        full_name = input("Please Enter the name of the famous individual? ")
    
    # Capitalize each word in full_name and save the result
    full_name = full_name.title()
    
    # String containing list of top 20 famous people
    famous_list = '''
Marilyn Monroe (1926 - 1962) American actress, singer, model
Abraham Lincoln (1809 - 1865) US President during American civil war
Nelson Mandela (1918 - 2013)  South African President anti-apartheid campaigner
John F. Kennedy (1917 - 1963) US President 1961 - 1963
Martin Luther King (1929 - 1968)  American civil rights campaigner
Queen Elizabeth II (1926 - ) British monarch since 1954
Winston Churchill (1874 - 1965) British Prime Minister during WWII
Donald Trump (1946 - ) Businessman, US President.
Bill Gates (1955 - ) American businessman, founder of Microsoft
Muhammad Ali (1942 - 2016) American Boxer and civil rights campaigner
Mahatma Gandhi (1869 - 1948) Leader of Indian independence movement
Margaret Thatcher (1925 - 2013) British Prime Minister 1979 - 1990
Mother Teresa (1910 - 1997) Macedonian Catholic missionary nun
Christopher Columbus (1451 - 1506) Italian explorer
Charles Darwin (1809 - 1882) British scientist, theory of evolution
Elvis Presley (1935 - 1977) American musician
Albert Einstein (1879 - 1955) German scientist, theory of relativity
Paul McCartney (1942 - ) British musician, member of Beatles
Queen Victoria ( 1819 - 1901) British monarch 1837 - 1901
Pope Francis (1936 - ) First pope from the Americas'''
  
    # Search famous_list for given name
    if famous_list.find(full_name) > 0:
        print(f"Yup, {full_name} did make the Top 20 cut!")
    else:
        print(f"Sorry, {full_name} did not make the Top 20 cut!")
        

def main():
    # Clear terminal window text in Windows OS
    os.system('cls')
    
    # Demonstrate completion of Module 6, Question 2
    Mod6_Q2()
    
    # Demonstrate completion of Module 6, Question 3
    Mod6_Q3()
    
    # Demonstrate completion of Module 6, Question 4
    print("\nQ4. HTML Strings with Tags:")
    print(add_html_tags("h1", "My First Page"))
    print(add_html_tags("p", "This is my first page."))
    print(add_html_tags("h2", "A secondary header."))
    print(add_html_tags("p", "Some more text."))

    # Demonstrate completion of Module 6, Question 5
    print("\nQ5. Greet Application:")
    # greet("alison", "smith") # Can remove these arguments to utilize user-input feature
    greet()
    
    # Demonstrate completion of Module 6, Question 6
    # abbreviate_middle_name("Elvis Aaron Presley") # Can remove this argument to utilize user-input feature
    abbreviate_middle_name()

    # Demonstrate completion of Module 6, Question 7
    print("\nQ7. Query Famous People:")
    # query_famous_people("Albert Einstein") # Can remove this argument to utilize user-input feature
    # query_famous_people("leonardo da vinci") # Can remove this argument to utilize user-input feature
    query_famous_people()  # Albert Einstein
    query_famous_people()  # leonardo da vinci

# Guard code: main() is only executed if this .py file is called directly (i.e., not imported as a module by another .py file)
if __name__ == "__main__":
    main()