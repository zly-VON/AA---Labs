import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from Spigot import calculate_pi_digit_S
from Gauss_Legendre import calculate_pi_digit_GL
from Bailey_Borwein_Plouffe import calculate_pi_digit_BBP

def calculate_pi_digit():
    n = [100, 500, 1000, 1500, 2000, 2500, 3000]
    time_alg1 = []
    time_alg2 = []
    time_alg3 = []

    for i in n:
        start_time = time.perf_counter()
        digit = calculate_pi_digit_BBP(i)
        time_alg1.append(round(time.perf_counter() - start_time, 5))

        start_time = time.perf_counter()
        digit = calculate_pi_digit_GL(i)
        time_alg2.append(round(time.perf_counter() - start_time, 5))

        start_time = time.perf_counter()
        digit = calculate_pi_digit_S(i)
        time_alg3.append(round(time.perf_counter() - start_time, 5))

    table = PrettyTable(['Name', '100', '500', '1000', '1500', '2000', '2500', '3000'])
    table.add_row(['BBP', time_alg1[0], time_alg1[1], time_alg1[2], time_alg1[3], time_alg1[4], time_alg1[5], time_alg1[6]])
    table.add_row(['Gauss-L', time_alg2[0], time_alg2[1], time_alg2[2], time_alg2[3], time_alg2[4], time_alg2[5], time_alg2[6]])
    table.add_row(['Spigot', time_alg3[0], time_alg3[1], time_alg3[2], time_alg3[3], time_alg3[4], time_alg3[5], time_alg3[6]])
    print(table)

    plt.plot(n, time_alg1, label='BBP')
    plt.plot(n, time_alg2, label='Gauss-L')
    plt.plot(n, time_alg3, label='Spigot')
    plt.xlabel('n-th Digit')
    plt.ylabel('Time (s)')
    plt.title('Calculate n-th Pi Digit Algorithms')
    plt.legend()
    plt.show()


calculate_pi_digit()