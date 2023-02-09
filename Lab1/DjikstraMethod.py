# Fibonacci Sequence Using Djikstra Formula

import time
import matplotlib.pyplot as plt

fib_table = []
time_table = []


def lucas_power(n: float):
    if n == 1:
        return (1, 1)
    L, F = lucas_power(n // 2)
    L, F = (L**2 + 5 * F**2) >> 1, L * F
    if int(n) & 1:
        return ((L + 5 * F) >> 1, (L + F) >> 1)
    else:
        return (L, F)


def djikstra(n: float):
    if int(n) & 1:
        return lucas_power(n)[1]
    else:
        L, F = lucas_power(n // 2)
    return L * F


fibs = {0: 0, 1: 1}


def fib(n: int):
    if n in fibs:
        return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2 * djikstra((n / 2) - 1)) + djikstra(n / 2)) * djikstra(n / 2)
        return fibs[n]
    else:
        fibs[n] = (djikstra((n - 1) / 2)**2) + (djikstra((n + 1) / 2)**2)


for n in range(5, 1005, 5):
    start_time = time.perf_counter()
    fib_table.append(n)
    x = fib(n)
    if n == 100: print('f({}) = {}'.format(n, x))
    time_table.append(time.perf_counter() - start_time)

plt.plot(fib_table, time_table, marker='o')
plt.ylabel('Time (s)')
plt.xlabel('n-th Fibonacci Term')
plt.title('Fibonacci Sequence Using Djikstra Formula')
plt.show()