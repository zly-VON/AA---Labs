# Fibonacci Sequence Iterative Method

import time
import matplotlib.pyplot as plt

fib_table = []
time_table = []


def fib(n):
    f = [0, 1]
    for k in range(2, n + 1):
        f.append(f[k-1] + f[k-2])
    return f[n]


for n in range(5, 1005, 5):
    start_time = time.perf_counter()
    fib_table.append(n)
    fib(n)
    time_table.append(time.perf_counter() - start_time)

plt.plot(fib_table, time_table, marker='o')
plt.ylabel('Time (s)')
plt.xlabel('n-th Fibonacci Term')
plt.title('Fibonacci Sequence Iterative Method')
plt.show()
