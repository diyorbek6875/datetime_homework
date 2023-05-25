#Task 5:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and determines the day of the week on which that date falls.
import datetime
a=int(input('kunni kiriting '))
b=int(input('oyni kiriting '))
c=int(input('yilni kiriting '))
data = datetime.date.today()
f1=abs(a-data.day)
f2=abs(b-data.month)*30
f3=abs(c-data.year)*365

farq=f1+f2+f3
if farq%7==3:
    print('Monday')
if farq%7==4:
    print("Tuesday")
if farq%7==5:
    print("Wednesday")
if farq%7==6:
    print('Thursday')
if farq%7==0:
    print("Friday")
if farq%7==1:
    print("Satuday ")
if farq%7==2:
    print("Sunday")