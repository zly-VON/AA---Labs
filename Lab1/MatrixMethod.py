# Fibonacci Sequence Matrix Power Method

import time
import matplotlib.pyplot as plt

fib_table = []
time_table = []


def fib(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    if (n == 0 or n == 1):
        return;
    M = [[1, 1],
         [1, 0]];

    power(F, n // 2)
    multiply(F, F)

    if (n % 2 != 0):
        multiply(F, M)


for n in range(5, 1005, 5):
    start_time = time.perf_counter()
    fib_table.append(n)
    fib(n)
    time_table.append(time.perf_counter() - start_time)

plt.plot(fib_table, time_table, marker='o')
plt.ylabel('Time (s)')
plt.xlabel('n-th Fibonacci Term')
plt.title('Fibonacci Sequence Matrix Power Method (Optimized)')
plt.show()