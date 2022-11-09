# Write a Program to display sum of all digits of a given Number N by user
num = int(input("Enter The Number : \n"))
number = num
sum = 0
while num!=0:
    digit = num % 10
    sum += digit
    num //= 10
print(f"The Sum Of Digits Of {number} is {sum}")