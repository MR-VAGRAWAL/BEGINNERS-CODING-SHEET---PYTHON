# Write a Program to Find GCD or HCF of two numbers
# entered by user
num1 = int(input("Enter The First Number : \n"))
num2 = int(input("Enter The Second Number : \n"))
factors_num1 = []
factors_num2 = []
common_factors = []
for i in range(1,num1+1):
    if num1 % i == 0:
        factors_num1.append(i)
# print(factors_num1)
for j in range(1,num2+1):
    if num2 % j == 0:
        factors_num2.append(j)
# print(factors_num2)
for k in range(len(factors_num1)):
    for l in range(len(factors_num2)):
        if factors_num1[k] == factors_num2[l]:
            common_factors.append(factors_num1[k])
# print(common_factors)
print(f"HCF OF {num1} and {num2} if {max(common_factors)}")