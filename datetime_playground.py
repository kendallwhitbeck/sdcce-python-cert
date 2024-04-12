# datetime module playground
import datetime
import pytz  # for time zones

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
now_loc = datetime.datetime.now()
print(f"now_loc={now_loc}")

# Using the now() method and pytz module to get the current date and time in UTC.
now_utc = datetime.datetime.now(pytz.UTC)
print(f"now_utc={now_utc}")

# Using the now() method and pytz module to get the current date and time in Sydney.
sydney_tz = pytz.timezone("Australia/Sydney")
now_syd = datetime.datetime.now(sydney_tz)
print(f"now_syd={now_syd}")

print("~~~~~~~~~~~~~~~")
# Using the strptime (string parse time) method to convert a string to a datetime object.
date_string = "22-5-2024"
date_object = datetime.datetime.strptime(date_string, "%d-%m-%Y")
# date_string = datetime.time("12:00 am")  # this will fail with TypeError
print(date_object)

print("\n~~~~~~~~Lecture 4/11~~~~~~~~~")
dt1 = datetime.datetime(2024, 4, 11, 18, 57)
print(dt1)

# Formatting date and time using strftime (string format time)
cur_time=datetime.datetime.now()
print(f"cur_time={cur_time}")
formatted_dt = cur_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
print(f"formatted_dt={formatted_dt}")


# from Python Docs website:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
dt = datetime.datetime.strptime('31/01/22 23:59:59.999999',
                  '%d/%m/%y %H:%M:%S.%f')
print(f"dt={dt}")


# using datetime objects to print "It was the summer of '69"
print("\n~~~~~~~ Summer of \'69 ~~~~~~~")
best_summer = datetime.datetime(1969, 6, 30)  # 30th June, 1969
print('Expected result  : It was the summer of \'69')  # easy way
print("catchy result    :", best_summer.strftime("It was the summer of \'%y"))  # short year datetime way
print("arrhythmic result:", best_summer.strftime("It was the summer of \'%Y"))  # long year datetime way


# Using strptime to convert a string to a datetime object with time of day
date_string_to_parse = "1969-06-30 8 pm"
parsed_time = datetime.datetime.strptime(date_string_to_parse, "%Y-%m-%d %I %p")
print(f"parsed_time={parsed_time}")

date_string_to_parse = "69-06-30 8 pm"
parsed_time = datetime.datetime.strptime(date_string_to_parse, "%y-%m-%d %I %p")
print(f"parsed_time={parsed_time}")


# Create timezone delta
tz_pdt = datetime.timedelta(hours=-7)  # 7 hours behind UTC = PDT
dt_pdt = datetime.datetime.now() + tz_pdt
print(f"dt_pdt={dt_pdt}")
