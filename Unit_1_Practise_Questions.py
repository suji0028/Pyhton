# Square Area Calculator
side = float(input("Enter the side of the square: "))
aos = side * side
print(f"The area of the Square is {aos}")

# Triangle Area Calculator
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height


print(f"The area of the triangle is {area}")

# Circle Area Calculator
ratio = float(input("Enter the ratio of circle: "))
pi = 3.14
aoc = pi * ratio ** 2
print(f"The area of the circle is {aoc}")

# Rectangle Area Calculator

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

aor = length * width

print(f"The area of the rectangle is {aor}")

# pieces into dozens
pieces = int(input("Enter pieces: "))
dozens = pieces // 12
left = pieces % 12
print(f"{dozens} dozen(s) and {left} piece(s)")

# Compound Interest Calculator
P = float(input("Enter the principal amount (₹): "))
r = float(input("Enter the annual interest rate (%): "))
t = float(input("Enter the time in years: "))

A = P * (1 + r / 100) ** t
CI = A - P

print(f"\nTotal Amount after {t} years: ₹{round(A, 2)}")
print(f"Compound Interest earned: ₹{round(CI, 2)}")
