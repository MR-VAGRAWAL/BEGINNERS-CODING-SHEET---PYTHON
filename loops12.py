# Write a Program to Check Whether a Number N
# entered by user is Palindrome or Not
num = int(input("Enter The Number : \n"))
number = num 
reverse_num = 0
while num!=0:
    reverse = num % 10
    reverse_num = reverse_num * 10 + reverse
    num //= 10
if number == reverse_num:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")