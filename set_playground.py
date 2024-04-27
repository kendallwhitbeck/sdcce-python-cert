# set_playground.py

color_choices = {"red", "orange", "yellow", "green", "blue", "indigo", "violet"}
print(f"color_choices = {color_choices}")

print('"red" in color_choices: ', end='')
print("red" in color_choices)

# set_a and set_b
set_a = {"A", "B", "C", "D"}
set_b = {"X", "B", "C", "Z"}
print(f"\nset_a = {set_a}")
print(f"set_b = {set_b}")

# Using set.difference() method
print("~ Using set.difference() method ~")
# Return the items in a, but not b
print(set_a.difference(set_b))
# Return the items in b, but not a
print(set_b.difference(set_a))

# Symmetric difference
print(set_a.symmetric_difference(set_b))
b_sym_diff_a = set_b.symmetric_difference(set_a)
print(b_sym_diff_a)

#  Order the set by converting to the list
list_b_sym_diff_a = list(b_sym_diff_a)
print(f"list_b_sym_diff_a={list_b_sym_diff_a}")
list_b_sym_diff_a.sort()
print(f"list_b_sym_diff_a={list_b_sym_diff_a}")

# Using set.intersection() method
print("\n~ Using set.intersection() method ~")
isect = set_a.intersection(set_b)
print(f"isect = {isect}")

# Using set.union() method
print("\n~ Using set.union() method ~")
a_union_b = set_a.union(set_b)  # has all the values from each set without duplicates
print(f"a_union_b = {a_union_b}")
print(f"color_choices = {color_choices}")
print(f"color_choices.union({'white', 'black'}) =\n{color_choices.union({'white', 'black'})}")

# Create a set using set()
building_in_question = set(["Building 3"])
building_in_question2 = {"Building 3"}
print(building_in_question == building_in_question2)

# # Use a set to remove duplicates and display which values were removed
original_list = [1, 2, 3, 3, 4, 5]
unique_set = set(original_list)
duplicates = []
# # DOES NOT WORK
for item in original_list:
    if item not in unique_set:
        duplicates.append(item)
# print(f"duplicates = {duplicates}")

# # DOES NOT WORK
# Convert the list to a set to remove duplicates
unique_set = set(original_list)
# Identify the items that were removed
removed_items = [item for item in original_list if item not in unique_set]
# Print the removed items
# # DOES NOT WORK
# print("Removed items:", removed_items)

for item in unique_set:
    if original_list.count(item) > 1:
        print(f"item = {item}; count = {original_list.count(item)}")

# using sorted() on a set
alphabet_set = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}  # has no particular order
sorted(alphabet_set)  # does not affect the set in later lines
print(alphabet_set)  # will print a set that is (probably) out of order (depending on the underlying hashmap)
print(sorted(alphabet_set))  # will print a list in order
print(sorted(alphabet_set, reverse=True))  # will be in reverse order
pass