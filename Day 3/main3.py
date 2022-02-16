#Write a program that works out whether if a given year is a leap year
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
year1 =str(year)
if (year % 4 == 0 and  year1[-2::] != "00"):
    print("Leap year")
elif (year % 400 == 0 and  year1[-2::] == "00"):
    print("Leap year")
else:
    print("Not leap year")
