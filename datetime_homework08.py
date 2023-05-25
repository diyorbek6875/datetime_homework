#Task 8:
#Write a Python program that subtracts 10 hours from the current time and displays the resulting time.
import datetime
data = datetime.datetime.today()
print(data.hour-10, data.minute)