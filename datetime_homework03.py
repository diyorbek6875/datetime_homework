#Task 3:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and calculates the number of days between the current date and the entered date.
import datetime
a=int(input('kunni kiriting '))
b=int(input('oyni kiriting '))
c=int(input('yilni kiriting '))
data = datetime.date.today()
#if data.day>=a:
 #   a1=data.day-a
#else :
#    a1=a-data.day
#if data.month>
f1=abs(a-data.day)
f2=abs(b-data.month)*30
f3=abs(c-data.year)*360
print(f1+f2+f3)
