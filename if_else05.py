# Write a Program to Check whether a year entered by user is Leap Year or no
year = int(input("Enter The Year Which You Want To Check :\n"))
if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
elif year % 4  == 0 :
     print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")