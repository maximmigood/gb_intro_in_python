# Вариант 1
sum_salary = 0
count = 0
print('*******************************************')
print('           Варинат 1')
print('*******************************************')
with open('task3.db', encoding='utf-8') as db:
    for row in db.readlines():
        second_name, salary = row.split()
        salary = float(salary)
        if salary < 20000:
            print(row.strip())
        sum_salary += salary
        count += 1
print('-------------------------------------------')
print(f'Средняя величина дохода сотрудников {sum_salary/count}')

# Вариант 2
print()
print('*******************************************')
print('           Варинат 2')
print('*******************************************')

with open('task3.db', encoding='utf-8') as db:
    table = [row.split() for row in db.readlines()]
table = [(r[0], int(r[1])) for r in table]
table2 = [f'{r[0]} {r[1]}' for r in table if r[1] < 20000]
print(*table2, sep='\n')

print(f'Средняя величина дохода сотрудников {sum(map(lambda x : x[1], table))/len(table)}')
