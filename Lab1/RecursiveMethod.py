# Fibonacci Sequence Recursive Method

import time
import matplotlib.pyplot as plt

fib_table = []
time_table = []


def fib(n):
    if n < 2: return n
    return fib(n - 1) + fib(n - 2)


for n in range(5, 21, 5):
    start_time = time.perf_counter()
    fib_table.append(n)
    fib(n)
    time_table.append(time.perf_counter() - start_time)


plt.plot(fib_table, time_table, marker='o')
plt.ylabel('Time (s)')
plt.xlabel('n-th Fibonacci Term')
plt.title('Fibonacci Sequence Recursive Method')
plt.show()


