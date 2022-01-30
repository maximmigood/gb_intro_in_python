from random import randint
n = 20
l = [randint(1, n // 2) for _ in range(n)]
print(l)
print([i for i in l if l.count(i) == 1])