# pandas_playground.py

import os
import pandas as pd

# Clear powershell terminal
os.system('cls')

# Create a random list. []
l = [2, 3, 5, 7, 11]

# Create a header. ()
l = ("Project Name", "Member Count", "Project Description")

def getGPS():
    """
    Returns the GPS coordinates (latitude, longitude, altitude) as a tuple.
    """
    # lat, lon, alt
    lat = 24.6
    lon = 117.9
    alt = 2000.0
    coordinates = (lat, lon, alt)
    return (coordinates)

print(getGPS(), end="; which is a data type: ")
print(type(getGPS()))

# Use pandas to read an excel file of GPS coordinates from subfolder 'data'.
gps_dataframe = pd.read_excel("data\gps_coords.xlsx")
# print(gps_dataframe)

# Access first row, first column of gps_coords.xlsx through data_frame.
# print(f"gps_dataframe.iloc[0,0] = {gps_dataframe.iloc[0,0]}")  # NOTE: dataframe.iloc[row, column] is a deprecated method
# print(f"gps_dataframe['Lat'].loc[0] = {gps_dataframe['Lat'].loc[0]}")  # This is the preferred method
# print(f"gps_dataframe['Lat'].loc[1] = {gps_dataframe['Lat'].loc[1]}")  # This is the preferred method

# Obtain the entire second row without using iloc[row, column]
print(f"gps_dataframe.loc[1]:\n{gps_dataframe.loc[1]}")

# List the items in gps_dataframe
# print(gps_dataframe.items())
# for element in gps_dataframe.items():
    # print(element)


"""
Count to 10 Example
"""
# Use pandas to read an excel file counting from 1 to 10 from subfolder 'data'.
count_10_data_frame = pd.read_excel("data\count_to_10.xlsx", header=None)
# print(count_10_data_frame.size)

"""
A1 to C6 Example
"""
print("\n~~~~~~~~~~~~~~~~~~~~~ A1 to C6 Example ~~~~~~~~~~~~~~~~~~~~~\n")
# Use pandas to read an excel file denoting cells A1 through C6
a1_c6_dataframe = pd.read_excel("data\cells_a1_to_c6.xlsx")  # this is incorrect: by looking at the data sheet, can tell we need to specify no header
a1_c6_dataframe_no_header = pd.read_excel("data\cells_a1_to_c6.xlsx", header=None)
# print(f"\na1_c6_dataframe:\n{a1_c6_dataframe}")
# print(f"\na1_c6_dataframe_no_header:\n{a1_c6_dataframe_no_header}")
for element in a1_c6_dataframe_no_header.items():
    print(element, "\n\n~~~\n")