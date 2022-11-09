# Write a Program to Display Prime Numbers Between Two Intervals (entered by user)
num1 = int(input("Enter The Starting Number : \n"))
num2 = int(input("Enter The Ending Number : \n"))
count = 0
for i in range(num1, num2+1):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(f"{i} is a prime number")