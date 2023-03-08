from math import sqrt

def alg5 (n):
    c = [True for i in range(n+1)]
    c[1] = False 
    i = 2
    while i <= n:
        j = 2
        while j <= sqrt(i):
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1