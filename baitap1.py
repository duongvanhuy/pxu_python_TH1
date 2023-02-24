import math
eps = 0.00001
i = 1
x = float(input("Nhập x: "))

first = 1
second = first + (x/math.factorial(i))

while (abs(first - second) > eps):
    i += 1
    first = second
    second = first + (x**i/math.factorial(i))

print("Giá trị là:", first)
