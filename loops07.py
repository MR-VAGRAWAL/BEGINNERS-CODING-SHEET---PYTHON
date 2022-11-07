# Write a Program to Find LCM of two numbers entered by user
num1 = int(input("Enter The Number : \n"))
num2 = int(input("Enter The Another Number : \n"))
greatest = 0
if num1 > num2 :
    greatest = num1
else:
    greatest = num2
while True:
    if (greatest % num1 == 0) and (greatest % num2 == 0):
        print(f"The LCM Of {num1} and {num2} is {greatest}")
        break
    greatest += 1