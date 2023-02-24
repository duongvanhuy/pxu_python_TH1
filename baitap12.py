import math
x = float(input("Nhap x: "))
step = 3
first = x
second = first + x**step / step

while abs(first - second) > 0.00000000000001:
    step += 2
    first = second
    second = first + x**step / step

print("S = ", first * 2)
