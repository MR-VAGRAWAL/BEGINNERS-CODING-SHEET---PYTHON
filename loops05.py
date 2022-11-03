# Write a Program to Display Fibonacci Series upto
# certain number n (n is entered by user)
fibonacci = [0 , 1]
num = int(input("Enter the terms till which you want series : "))
for i in range(3,num+1):
    value = fibonacci[i-2] + fibonacci[i-3]
    fibonacci.append(value)
print(fibonacci)