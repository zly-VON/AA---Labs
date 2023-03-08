import time
from algorithm.algorithm_1 import alg1
from algorithm.algorithm_2 import alg2
from algorithm.algorithm_3 import alg3
from algorithm.algorithm_4 import alg4
from algorithm.algorithm_5 import alg5
import matplotlib.pyplot as plt
from prettytable import PrettyTable


def Eratosthenes():
    n = [10, 100, 500, 1000, 5000, 10000, 50000, 100000]
    time_alg1 = []
    time_alg2 = []
    time_alg3 = []
    time_alg4 = []
    time_alg5 = []

    for i in n:
        start_time = time.perf_counter()
        alg1(i)
        time_alg1.append(round(time.perf_counter() - start_time, 5))

        start_time = time.perf_counter()
        alg2(i)
        time_alg2.append(round(time.perf_counter() - start_time, 5))

        start_time = time.perf_counter()
        alg3(i)
        time_alg3.append(round(time.perf_counter() - start_time, 5))

        start_time = time.perf_counter()
        alg4(i)
        time_alg4.append(round(time.perf_counter() - start_time, 5))

        start_time = time.perf_counter()
        alg5(i)
        time_alg5.append(round(time.perf_counter() - start_time, 5))
    
    
    table = PrettyTable(['Name', '10', '100', '500', '1000', '5000', '10000', '50000', '100000'])
    table.add_row(['Alg1', time_alg1[0], time_alg1[1], time_alg1[2], time_alg1[3], time_alg1[4], time_alg1[5], time_alg1[6], time_alg1[7]])
    table.add_row(['Alg2', time_alg2[0], time_alg2[1], time_alg2[2], time_alg2[3], time_alg2[4], time_alg2[5], time_alg2[6], time_alg2[7]])
    table.add_row(['Alg3', time_alg3[0], time_alg3[1], time_alg3[2], time_alg3[3], time_alg3[4], time_alg3[5], time_alg3[6], time_alg3[7]])
    table.add_row(['Alg4', time_alg4[0], time_alg4[1], time_alg4[2], time_alg4[3], time_alg4[4], time_alg4[5], time_alg4[6], time_alg4[7]])
    table.add_row(['Alg5', time_alg5[0], time_alg5[1], time_alg5[2], time_alg5[3], time_alg5[4], time_alg5[5], time_alg5[6], time_alg5[7]])
    print(table)

    plt.plot(n, time_alg1, label='alg1')
    plt.plot(n, time_alg2, label='alg2')
    plt.plot(n, time_alg3, label='alg3')
    plt.plot(n, time_alg4, label='alg4')
    plt.plot(n, time_alg5, label='alg5')
    plt.xlabel('n Prime Numbers')
    plt.ylabel('Time (s)')
    plt.title('Sieve of Eratosthenes Algorithms')
    plt.legend()
    plt.show()


Eratosthenes()