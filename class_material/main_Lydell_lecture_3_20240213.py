#
# Author: Lydell Aaron
# Assignment: Module 2 Question 1
# Description: Describe the files here...
#

# Read strings from the user
age_str = input("Enter your age")

# Convert strings to variables
age = float(age_str)

if age > 70:
    health_str = input("How is your health: 0 bad, 1 good")
    health = int(health_str)

    # If in good health, give maximum benefit...
    print(health)
    print(type(health))

    if health == 1:
        print("Max benefit")
    elif health == 0:
        print("Sub max benefit")
    else:
        print("Err: Unknown health option")

elif (age <= 70) and (age > 59.5):
    # Perform table calculation here
    print("% of benefit")
elif age <= 59.5:
    print("Max penalty")
else:
    print("Unknown state")
