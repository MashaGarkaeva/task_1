import math
import matplotlib.pyplot as plt

x = []
y = []
up = []
low = []
start = -3.14
end = 3.14
step = (3.14 + 3.14) / 99

current = start
while current <= end:
    x.append(current)

    sin_x = math.sin(current * 12) * 5

    sin_ul = math.sin(current) + 2
    up.append(sin_ul)

    sin_ll = -sin_ul - 2
    low.append(sin_ll)

    if sin_ll <= sin_x <= sin_ul:
        y.append(sin_x)
    elif sin_x < sin_ll:
        y.append(sin_ll)
    else:
        y.append(sin_ul)

    current += step

plt.plot(x, y, '--')
plt.plot(x, up)
plt.plot(x, low)
plt.show()