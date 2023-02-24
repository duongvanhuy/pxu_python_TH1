import math
x = float(input("Nhap x: "))
step = 3
i = 0
first = x
second = (first - x**step / step)

while abs(first - second) > 0.000000001:
    step += 2
    i += 1
    first = second
    if (i % 2 != 0):
        second = first + x**step / step
    else:
        second = first - x**step / step

print("S = ", first)
