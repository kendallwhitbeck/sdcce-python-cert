# Data Collections Playground

import datetime
import os

# Clear the terminal in Windows powershell
os.system('cls')

# List - use square brackets `[]` to create a list
grocery_list = [5, 6, 56, "apple", datetime.datetime(2024, 4, 16)]
# Use append to add an item to the end of the list
grocery_list.append("banana")
# Display grocery list
for item in grocery_list:
    print(item)

# Use the extend method to add multiple items to the end of the list
print("\n~~~~~~~~~~~ Larger Grocery List ~~~~~~~~~~")
fruit_list = ["apple", "orange", "watermelon"]
bread_list = ["wheat", "rye", "sourdough"]
larger_grocery_list = list()
larger_grocery_list.extend(fruit_list)
larger_grocery_list.extend(bread_list)
for item in larger_grocery_list:
    print(item)

# this creates a nested list
print("\n~~~~~~~~~~~ Nested Grocery List ~~~~~~~~~~")
nested_grocery_list = list()
# nested_grocery_list = [fruit_list, bread_list]  # equivalent to
nested_grocery_list.append(fruit_list)
nested_grocery_list.append(bread_list)
for item in nested_grocery_list:
    print(item)
# I want sourdough!
print(f"give me {nested_grocery_list[1][2]}!")

# Using insert, pop, and remove list methods
print("\n~~~~~~~~~~~ Insert, Pop, and Remove List Methods ~~~~~~~~~~")
print("start with larger_grocery_list:")
print(larger_grocery_list)
print("insert 'spinach' at index 3:")
save_inserted_value = larger_grocery_list.insert(3, "spinach")  # value is None
print(larger_grocery_list)
print("remove 'wheat' from larger_grocery_list:")
save_removed_value = larger_grocery_list.remove("wheat")  # value is None
print(larger_grocery_list)
print("pop 'rye' from larger_grocery_list:")
save_popped_value = larger_grocery_list.pop(4)
print(larger_grocery_list)
# Display saved values
print("saved values:")
print(f"save_inserted_value={save_inserted_value}")
print(f"save_removed_value={save_removed_value}")
print(f"save_popped_value={save_popped_value}")

# Using index list method to find index of item in list
print("\n~~~~~~~~~~~ Index List Method ~~~~~~~~~~")
print(larger_grocery_list)
print(f"index of 'spinach' in larger_grocery_list: {larger_grocery_list.index('spinach')}")

# Using list's sort method with reverse keyword.
print("\n~~~~~~~~~~~ Reverse List Method ~~~~~~~~~~")
count_to_5 = [1, 2, 3, 4, 5]
count_to_5.sort(reverse=True)
print(count_to_5)  # Outputs: [5, 4, 3, 2, 1]

alphabets = ['a','e','d','c','b']
alphabets.sort()
print(alphabets)

random_numbers = [2,5,6,1,8,3]
random_numbers.sort()
print(random_numbers)
