print('Вводите строки. Когд закончите введите пустую строку.')
z = [input()]
while z[-1]:
    z.append(input())
with open('task1.txt', 'w') as file_obj:
    file_obj.write('\n'.join(z[:-1]))
