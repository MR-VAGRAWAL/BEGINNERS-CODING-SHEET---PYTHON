# Write a Program to check whether a number entered by the user is an Armstrong number or not.
num = int(input("Enter The Number : \n"))
number = num
org_num = num
armstrong = 0
count = 0
while num!=0:
    digit = num % 10
    num //= 10
    count += 1
while number!=0:
    digit = number % 10
    armstrong += digit**count
    number //= 10
print(armstrong)
if armstrong == org_num:
    print(f"{org_num} is a armstrong number")
else:
    print(f"{org_num} is not a armstrong number")