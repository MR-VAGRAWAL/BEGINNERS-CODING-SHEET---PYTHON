#  Write a Program to Find Factorial of a given number N
# (N is entered by user)
num = int(input("Enter The Number : \n"))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
print(f"Factorial of {num} is {factorial}")