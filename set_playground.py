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

