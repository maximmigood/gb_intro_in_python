def fact(n):
    r = 1
    for i in range(1, n+1):
        r *= i
        yield r


for e in fact(15):
    print(e)
