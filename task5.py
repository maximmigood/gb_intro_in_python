from random import random
n = 50000
with open('task5.txt', 'w') as obj_file:
    obj_file.writelines(' '.join([str(random()*10-5) for _ in range(n)]))

with open('task5.txt', 'r') as obj_file:
    z = obj_file.readline();
z = z.split()
s = sum(map(float, z))

#print(s, s / len(z), len(z))
