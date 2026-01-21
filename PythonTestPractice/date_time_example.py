# date_time_example.py

from datetime import datetime, timedelta

# Step 1: Get current date and time
now = datetime.now()
print("Current Date and Time:", now)

# Step 2: Format date and time
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted)

# Step 3: Extract specific components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Step 4: Add or subtract time using timedelta
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)

# Step 5: Parse a string into a datetime object
date_string = "2026-01-19 15:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date:", parsed_date)

# Step 6: Difference between two dates
difference = tomorrow - yesterday
print("Difference between tomorrow and yesterday:", difference)