#Task 9:
#Write a Python program that calculates the difference between two given dates. Prompt the user to enter two dates in the format "dd-mm-yyyy" and display the number of days between them.
import datetime
a1=int(input("Dastlabki kunni "))
b1=int(input('dastlabki oy '))
c1=int(input('dastlabki yil '))
a2=int(input("keyingii kunni "))
b2=int(input('keyingi oy '))
c2=int(input('keyingi yil '))
f1=abs(a1-a2)
f2=abs(b1-b2)*30
f3=abs(c1-c2)*365   
farq=f1+f2+f3
print(farq)