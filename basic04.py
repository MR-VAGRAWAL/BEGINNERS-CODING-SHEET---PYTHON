# Write a program where the user is asked to enter two
# integers (divisor and dividend) and the quotient and the
# remainder of their division is computed.(Both divisor and
# dividend should be integers.)
divisor = int(input("Enter the divisor:\n"))
dividend = int(input("Enter the dividend:\n"))
quotient = dividend // divisor
remainder = dividend % divisor
print(f"If the Divisor is {divisor} and Dividend is {dividend} then the Quotient will be {quotient} and Remainder will be {remainder}")