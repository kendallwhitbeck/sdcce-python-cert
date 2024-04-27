# -*- coding: utf-8 -*-
"""
Author: Kendall Whitbeck
Student ID: 5550203278
Assignment: Module 1, Question 1
Description:
This program calculates the estimated duration of a trip in hours and minutes (same time zone).
This should include an estimated date/time of departure and an estimated date/time of arrival:
    For the date of departure and arrival, the program should use the YYYY-MM-DD format for dates.
    For the time of departure and arrival , the program should use the HH:MM AM/PM format for times.
    For the miles and miles per hour, the program should only accept integer entries like 200 and 65.
    Assume that the user will enter valid data (no error handling).
"""

import os  # os.system('cls'): clear terminal window text in Windows OS
from datetime import datetime, timedelta  # datetime objects

def estimate_arrival_time():
    """
    Calculate the estimated duration of a trip in hours and minutes.
    """
    # Collect inputs
    date_depart_str = input("Estimated date of departure (YYYY-MM-DD): ")  # 2019-3-15
    time_depart_str = input("Estimated time of departure (HH:MM AM/PM): ")  # 11:00 AM
    miles = int(input("Enter miles: "))  # 500
    speed_mph = int(input("Enter miles per hour: "))  # 70

    # Convert date and time strings to datetime objects
    datetime_depart = datetime.strptime(date_depart_str + " " + time_depart_str, "%Y-%m-%d %I:%M %p")

    # Calculate estimated travel time
    print("\nEstimated travel time")
    travel_time = miles / speed_mph
    hours_int = int(travel_time)
    minutes_int = int((travel_time - hours_int) * 60)

    # Display estimated travel time
    print(f"Hours: {hours_int}")
    print(f"Minutes: {minutes_int}")

    # Calculate estimated arrival date and time
    timedelta_travel_time = timedelta(hours=hours_int, minutes=minutes_int)
    datetime_arrival = datetime_depart + timedelta_travel_time

    # Display estimated arrival date and time
    print(f"Estimated date of arrival: {datetime_arrival.strftime('%Y-%m-%d')}")
    print(f"Estimated time of arrival: {datetime_arrival.strftime('%I:%M %p')}")

def main():
    # Clear terminal window text in Windows OS
    os.system('cls')

    # Continuously prompt user for estimating arrival date and time until they choose to exit
    print("Arrival Time Estimator")
    while True:
        estimate_arrival_time()
        if input("\nContinue? (y/n): ").lower() != 'y':
            break
        print("")
    print("Bye!")

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file)
if __name__ == "__main__":
    main()