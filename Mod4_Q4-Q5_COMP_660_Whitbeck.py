"""
Author: Kendall Whitbeck
Student ID: 5550203278
Assignment: Module 4 Questions 4-5
Description: This program contains functions for calculating final velocity and elapsed time for a dropped ball.
"""

def velocityFinal(u, a, d):
    '''
    This function returns final velocity given initial velocity, acceleration and distance.
    
    Parameters:
    u (float): The initial velocity in m/s.
    a (float): The uniform acceleration in m/s^2.
    d (float): The distance traveled in m.
    
    Returns:
    v (float): The final velocity rounded to 1 decimal place in m/s.
    '''
    v = (u ** 2 + 2 * a * d) ** 0.5
    return round(v,1)

def elapsedTime(v, u, a):
    '''
    This function returns elapsed time given final velocity, initial velocity and acceleration.
    
    Parameters:
    v (float): The final velocity in m/s.
    u (float): The initial velocity in m/s.
    a (float): The uniform acceleration in m/s^2.
    
    Returns:
    t (float): The elapsed time rounded to 1 decimal place in s.
    '''
    t = (v - u) / a
    return round(t,1)

# Initial Conditions of the dropped ball:
u = 0 # initial speed of the ball in m/s.
g = 9.8 # acceleration due to gravity in m/s^2.
h = 51 # height from which the ball is dropped in m.

# 4.b: The calling expression to determine the final velocity of the ball before impact:
v = velocityFinal(u, g, h)

# 4.c: The value of the final velocity of the ball before impact:
print(f"\nThe final velocity of the ball is {v} m/s.")

# 5: Calculate the elapsed time from when the ball is dropped until it hits the ground:
t = elapsedTime(v, u, g)
print(f"\nThe elapsed time from when the ball is dropped until it hits the ground is {t} s.\n")