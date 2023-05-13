from decimal import Decimal, getcontext

def calculate_pi_digit_GL(n):
    getcontext().prec = n + 10  # Set precision to n+10 to ensure accuracy

    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(0.25)
    p = Decimal(1)

    for _ in range(n):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

    pi = (a + b) ** 2 / (4 * t)
    pi_str = str(pi)
    return int(pi_str[n+2])
