# datetime module playground
import datetime

t1 = datetime.datetime(2024, 4, 9, 12, 0, 0)
d1 = datetime.timedelta(weeks=1)

# Calculate resulting time A from t1 and a timedelta duration of 1 week.
ta = t1 + d1
print(f"t1={t1}")
print(f"d1={d1}")
print(f"ta={ta}")

t2 = datetime.datetime(2024, 4, 9)
print(f"t2={t2}")

d3 = t2 - t1
print(f"i3={d3}")
print(type(d3))

print("~~~~~~~~~~~~~~~")
day_start = datetime.date(2024, 4, 9)
t_start = datetime.time(19, 47, 0)
print(day_start)
print(t_start)

print("~~~~~~~~~~~~~~~")
# t1 = datetime.datetime("aug 2015")
t1 = datetime.datetime(2015, 1, 1, 12, 0, 0)
print("t1=", t1)

print("~~~~~~~~~~~~~~~")
# Using the now() method to get the current date and time.
now = datetime.datetime.now()
print(f"now={now}")

print("~~~~~~~~~~~~~~~")
# Using the strptime method to convert a string to a datetime object.
date_string = "22-5-2024"
date_object = datetime.datetime.strptime(date_string, "%d-%m-%Y")
# date_string = datetime.time("12:00 am")  # this will fail with TypeError
print(date_object)
