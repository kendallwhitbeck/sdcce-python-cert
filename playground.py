'''
Use: experimenting w/ code
'''

from os import *

print("Hello World")

pass # TBD

# map()

print(3 ^ 1)

def oddNumbers(l, r):
    # If l is even, then increment to the next odd number since range() is inclusive of `start` variable
    if l % 2 == 0:
        l += 1

    # If r is odd, then increment to next even number since range() is exclusive of `stop` variable
    if r % 2 == 1:
        r += 1

    # Return odd numbers between l and r where l is the left bound and r is the right bound
    return range(l, r, 2)

ar = [1,2,3,4]
sum = 0
for i in range(len(ar)):
    # print(f"i={i}")
    sum += ar[i]
#     print(f"sum={sum}")
# print(f"final sum={sum}")
# print(range(len(ar)))

print("B = ", ord("B"))
# print(ord(66))

counting = "54321"
print("Countdown...")
for char in counting:
    print(char + "...")
print("Blastoff!")

s1 = "abc def ghi";
s2 = s1[1:5]
s3 = s2.replace('b', 'z')
print(s3)

email = "marytechknowsolve.com"
result = email.find("@")
print(result)

print(oddNumbers(2, 5))

"""
Module 7 Discussion
"""
print("\nModule 7 Discussion")
# The // operator performs integer division or floor division. It divides two numbers then returns the largest integer that is less than or equal to the quotient. Example:
result = 7 // 2.0
print(result)  # Output: 3

# The % operator computes the remainder of one number divided by another. Example:
result = 7 % 2
print(result)  # Output: 1
if 10 % 2 == 0:
    print("10 is even")
if 11 % 2 == 1:
    print("11 is odd")

# The ** operator performs exponentiation of one number to the power of another. Example:
result = 7 ** 2  # equivalent to (7^2) in arithmetic
print(result)  # Output: 49

# Three examples of number systems not including decimal are: binary, octal, and hexadecimal.
binary_number = 0b101
print(binary_number)  # Output: 5

octal_number = 0o12
print(octal_number)  # Output: 10

hexadecimal_number = 0x1b
print(hexadecimal_number)  # Output: 27

# someone else's example
bin_no1 = 100110
bin_no2 = 1101
print(f"bin_no1 + bin_no2 = '{bin_no1 + bin_no2}'")
addition_result = bin(bin_no1 + bin_no2)
print(bin(101211))
# bin_no1 = 0b100110
# bin_no2 = 0b1101
# addition_result = bin(bin_no1 + bin_no2)
print(addition_result)

number = 3237945.76
print("option 1")
print("{:,.4f}".format(number))
print("option 2")
print("{:25,.9f}".format(number))
print("option 3")
print("{:,.2f}".format(number))
print("option 4")
print("{:.2f}".format(number))

print("\n~~~~~~~~~~~~~\nRMS Velocity redo:")
import scipy.constants  # R (molar gas constant)
import decimal
def calc_rms_vel(temp_C, molar_mass):
    temp_K = temp_C + 273.15  # Temperature in Kelvin
    R = 8.3145  # Ideal Gas Constant
    print(f"scipy.constants.gas_constant = {scipy.constants.gas_constant}")
    rms_vel = (3 * R * temp_K / molar_mass) ** (1/2)
    print("rms_vel = {:}; type = {:}".format(rms_vel, type(rms_vel)))
    rms_vel_dec = decimal.Decimal(rms_vel)
    print(f"RMS Vel decimal = {rms_vel_dec}; type = {type(rms_vel_dec)}")
    rms_vel_quantized = rms_vel_dec.quantize(decimal.Decimal('100.000'))
    print(f"RMS Vel quantized = {rms_vel_quantized}; type = {type(rms_vel_quantized)}")
temp_C = 25
molar_mass = 3.2e-2
calc_rms_vel(temp_C, molar_mass)
