#  Write a Program to Generate Multiplication Table of a
# number (entered by the user) using a for loop.
num = int(input("Enter The Number : "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")