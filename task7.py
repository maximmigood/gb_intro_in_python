sum_profit = 0
count = 0
d = {}

with open('task7.txt', 'r', encoding='utf-8') as obj_file:
    for row in obj_file.readlines():
        r = row.split()
        revenue = float(r[2])
        cost = float(r[3])
        profit = revenue - cost
        d[r[0]] = profit
        sum_profit += max(0, profit)
        count += 1
res = [d, {'average_profit': sum_profit / count}]
print(res)
