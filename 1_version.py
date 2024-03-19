import math
from array import array
import matplotlib.pyplot as plt
import numpy as np

'''
plt.grid()
x = np.linspace(-3.14, 3.14, 99)
y = np.sin(x)
y1 = np.sin(x) + 3
a = np.sin(x) * np.sin(y + y1) * -4

plt.plot( x, y, '--')
plt.plot( x, y1)
plt.plot(x, a)

plt.show()'''

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
    sin_x = math.sin(current * 3)
    y.append(sin_x)

    sin_ul = math.sin(current)
    up.append(max(sin_x, sin_ul))
    low.append(sin_ul)

    current += step

plt.plot(x, y)
plt.plot(x, up)
plt.plot(x, low)
plt.show()