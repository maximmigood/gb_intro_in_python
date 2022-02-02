changes = {'One': 'Один', 'Two': 'Два', 'Three': 'Трии', 'Four': 'Четыре'}

with open('task4.txt', 'r') as obj_file:
    z = obj_file.readlines()

    res = [a.split() for a in z]
    res = map(lambda x: [changes[x[0]], x[1], x[2]], res)
    res = map(lambda x: ' '.join(x), res)

with open('task4_.txt', 'w', encoding='utf-8') as obj_file:
    obj_file.writelines('\n'.join(res))
