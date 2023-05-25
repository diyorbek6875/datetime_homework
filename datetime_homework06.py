#Task 6:
#Write a Python program that accepts a date in the format "dd-mm-yyyy" and checks if it is a leap year. Display an appropriate message indicating whether it is a leap year or not.
import datetime

c=int(input('yilni kiriting '))
data = datetime.date.today()

f3=abs(c-data.year)
if f3%4==3:
    print("Maskur yil kabisa yili ")
else :
    print("Bu yil kabisa yili emas ")

