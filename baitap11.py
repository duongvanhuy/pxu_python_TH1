import math
x = float(input("Nhap x: "))
step = 2
first = x
second = (first - x**step / step)

while abs(first - second) > 0.0001:
    step += 1
    first = second
    if (step % 2 != 0):
        second = first + x**step / step
    else:
        second = first - x**step / step

print("S = ", first)
