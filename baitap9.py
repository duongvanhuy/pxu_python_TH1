import math
x = float(input("Nhap x: "))
step = 2
i = 0
first = 1
second = (first - x**step / math.factorial(step+1))

while abs(first - second) > 0.00000000001:
    step += 2
    i += 1
    first = second
    if (i % 2 != 0):
        second = first + x**step / math.factorial(step+1)
    else:
        second = first - x**step / math.factorial(step+1)

print("S = ", first)
