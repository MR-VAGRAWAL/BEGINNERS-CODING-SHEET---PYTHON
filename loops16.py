#  Write a Program to Display all Factors of a Number entered by User.
num = int(input("Enter The Number : \n"))
print(f"The Factors of {num} are : ")
for div in range(1,num+1):
    if num % div == 0:
        print(div)