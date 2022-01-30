from functools import reduce
start = 100
finish = 1000
l = [a for a in range(start, finish + 1) if a % 2 == 0]
z = reduce(lambda x, y: x * y, l)
print(z)