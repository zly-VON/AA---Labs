from decimal import Decimal, getcontext

def calculate_pi_digit_BBP(n):
    getcontext().prec = n + 10  # Set precision to n+10 to ensure accuracy

    pi = Decimal(0)
    k = 0

    while True:
        term = (Decimal(1)/(16**k)) * (
                (Decimal(4)/(8*k+1)) -
                (Decimal(2)/(8*k+4)) -
                (Decimal(1)/(8*k+5)) -
                (Decimal(1)/(8*k+6))
        )
        pi += term

        if k >= n:
            break

        k += 1

    pi_str = str(pi)
    return int(pi_str[n+2])
