# Fibonacci Sequence Kartik’s K sequence Method (K=3)

import time
import matplotlib.pyplot as plt

fib_table = []
time_table = []


def fib(n):
    n1, n2 = 1, 1
    if n > 3:
        for _ in range((n // 3)):
            n1, n2 = n2, (n2 << 2) + n1
    if n % 3 == 0:
        return n1
    elif n % 3 == 1:
        return (n2 - n1) >> 1
    elif n % 3 == 2:
        return (n2 + n1) >> 1


for n in range(5, 1005, 5):
    start_time = time.perf_counter()
    fib_table.append(n)
    fib(n)
    time_table.append(time.perf_counter() - start_time)

plt.plot(fib_table, time_table, marker='o')
plt.ylabel('Time (s)')
plt.xlabel('n-th Fibonacci Term')
plt.title('Fibonacci Sequence Kartik’s K sequence Method')
plt.show()
