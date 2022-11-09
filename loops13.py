# Write a Program to Check Whether a Number is Prime or Not
num = int(input("Enter The Number :\n"))
count_div = 0
for div in range(1,num+1):
    if (num % div == 0):
        count_div += 1
if count_div == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")