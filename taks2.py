from random import randint
n = 20
lst = [randint(0, n) for _ in range(n)]
print(f'{lst=:}')
lst2 = [lst[i] for i in range(1, n) if lst[i] > lst[i - 1]]
print(f'{lst2=:}')