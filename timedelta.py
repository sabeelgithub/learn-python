from datetime import datetime

now = datetime.now()
print(now)


# Access individual components of a datetime object
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)

# Format a datetime object as a string
formatted = now.strftime('%Y-%m-%d %H:%M:%S')
print(formatted)



from datetime import date

# Create a date object for a specific date
d = date(2023, 6, 18)
print(d)


# Access individual components of a date object
year = d.year
month = d.month
day = d.day

# Format a date object as a string
formatted = d.strftime('%Y-%m-%d')

from datetime import time

# Create a time object for a specific time
t = time(12, 30, 0)

print(t)

# Access individual components of a time object
hour = t.hour
minute = t.minute
second = t.second

# Format a time object as a string
formatted = t.strftime('%H:%M:%S')


from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()

# Create a timedelta representing a duration of 5 days
five_days = timedelta(days=5)

# Add the timedelta to the current date and time
future = now + five_days
print(future)

# Calculate the difference between two dates or times
diff = future - now
print(diff)
