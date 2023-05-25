#Task 7:
#Write a Python program that adds 5 days to the current date and displays the resulting date.
import datetime
data = datetime.date.today()
print(data.day+5,data.month,data.year)