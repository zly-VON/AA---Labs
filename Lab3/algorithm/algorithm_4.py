def alg4 (n):
    c = [True for i in range(n+1)]
    c[1] = False
    i = 2
    while i <= n:
        j = 2
        while j < i and c[i]:
            if i % j == 0:
                c[i] = False
            j = j + 1
        i = i + 1