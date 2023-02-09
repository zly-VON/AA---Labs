# Fibonacci Sequence Binet Method

import math
import time
import matplotlib.pyplot as plt

fib_table = []
time_table = []


def fib(n):
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))


for n in range(5, 105, 5):
    start_time = time.perf_counter()
    fib_table.append(n)
    fib(n)
    time_table.append(time.perf_counter() - start_time)

plt.plot(fib_table, time_table, marker='o')
plt.ylabel('Time (s)')
plt.xlabel('n-th Fibonacci Term')
plt.title('Fibonacci Sequence Binet Method')
plt.show()
