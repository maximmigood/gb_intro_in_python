my_list = [7, 5, 3, 3, 2]
num = int(input('Введите число для добавления в рейтинг: '))

for i in range(len(my_list)):
    if my_list[i] <= num:
        my_list.insert(i, num)
        break
else:
    my_list.append(num)

print(*my_list)
