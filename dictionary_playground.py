# dictionary_playground.py

about_me = {
    "name": "Kendall",
    "favorite_color": "orange",
    "favorite_hobby": "travel"
}
print(f"about_me =\n{about_me}\n")

# creating dictionary with varying data types
pizza_order = {
    "order_no": 12345,
    "size": "large",
    "type": "margherita",
    "price": 12.99
}
print(f"pizza_order =\n{pizza_order}\n")

# loop through dictionaries
print("~ loop through dictionaries ~")
counter = 0
for key in pizza_order.keys():
    counter +=1
    print(f"key {counter}={key}")
counter = 0
for value in pizza_order.values():
    counter +=1
    print(f"value {counter} = {value}")
counter = 0
for key, value in pizza_order.items():
    counter +=1
    print(f"{counter}: key = {key}; value = {value}")

# use enumerate() method on dictionary
print("\n~ use enumerate() method on dictionary ~")
for enum in enumerate(pizza_order):  # defaults to keys, not values
    print(f"enum = {enum}")
print("~ use enumerate() method on dictionary.keys() ~")
for enum in enumerate(pizza_order.keys()):  # same as not specifying keys() method, as in previous loop
    print(f"enum = {enum}")
print("~ use enumerate() method on dictionary.values() ~")
for enum in enumerate(pizza_order.values()):
    print(f"enum = {enum}")
print("~ use enumerate() method on dictionary.values() ~")
for idx, val in enumerate(pizza_order.values()):
    print(f"idx = {idx}", end=", ")
    print(f"val = {val}")
