# Write a Program to Calculate Power of a Number
# without using inbuilt pow() function by taking two
# inputs from users as Base and exponent respectively
base = int(input("Enter The Base Number : \n"))
exponent = int(input("Enter The Exponent Number : \n"))
result = 1
for exponent in range(exponent,0,-1):
    result*=base
print(result)