def alg1 (n):
    c = [True for i in range(n+1)]
    c[1] = False 
    i = 2
    while i <= n:
        if c[i] == True:
            j = 2 * i
            while j <= n:
                c[j] = False
                j += i
        i += 1