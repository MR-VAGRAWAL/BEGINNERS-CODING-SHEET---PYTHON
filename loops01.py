#  Write a Program to Calculate Sum of first N Natural
# Numbers (here value of N is Entered by user)
num = int(input("Enter The Number Till Which You Want Sum : "))
sum = 0
for i in range(1 , num+1):
    sum = sum + i
print(f"Sum of first {num} namtural number is {sum}")