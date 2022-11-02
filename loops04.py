# Write a Program to Display Fibonacci Series upto nth
# term (n is entered by user)
fibonacci = [0 , 1]
n = int(input("Enter The term till which you want the series : "))
for term in range(3,n+1):
    value = fibonacci[term-2] + fibonacci[term-3]
    fibonacci.append(value)
print(fibonacci)