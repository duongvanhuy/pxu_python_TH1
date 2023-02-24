import math
x = float(input("Nhap x: "))
step = 2
first = x
second = first + x**step / math.factorial(step)

while abs(first - second) > 0.0001:
    step += 2
    first = second
    second = first + x**step / math.factorial(step)

print("S = ", first)
