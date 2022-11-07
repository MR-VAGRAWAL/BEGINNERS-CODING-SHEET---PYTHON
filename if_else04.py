#  Write a Program which accepts coefficients of a
# quadratic equation from the user and displays the roots
# (both real and complex roots depending upon the
# discriminant).
a = int(input("Enter The Cofficient Of x**2 :\n"))
b = int(input("Enter The Cofficient Of x :\n"))
c = int(input("Enter The Constant Value :\n"))
eqn = f"{a}x**2 + {b}x + {c}"
print(eqn)
d = ((b**2)-4*a*c)
if d >= 0:
    root1 = (-b+((b**2)-4*a*c)**0.5)/2*a
    root2 = (-b-((b**2)-4*a*c)**0.5)/2*a
    print(f"The Roots Of The {eqn} is {root1} and {root2}")
else:
    print("The Equation Will Hve Imaginary Roots")