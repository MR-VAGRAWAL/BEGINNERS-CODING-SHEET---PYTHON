# Write a Program to Reverse a given Number N by user
num = int(input("Enter The Number : \n"))
while num!=0:
    reverse = num % 10
    print(reverse,end = "")
    num //= 10