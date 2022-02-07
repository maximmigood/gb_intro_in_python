res = {}

with open('task6.txt', 'r', encoding='utf-8') as obj_file:
    for row in obj_file.readlines():
        r = row.split()
        res[r[0][:-1]] = sum([int(a.split('(')[0]) for a in r if a[0].isdigit()])
print(res)
