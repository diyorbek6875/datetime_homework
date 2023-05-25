#Task 4:
#Write a Python program that calculates the age of a person based on their birth year. Prompt the user to enter their birth year, and display their current age.
import datetime
a=int(input("Tug'ilgan yilingizni kiriting "))
data=datetime.date.today()
yoshi= data.year-a
print(yoshi)
