products = []
# Собираем данные
i = 1
while True:
    ans = input('Будете вводить данные о товаре? (N(nНн) - Выход): ')
    if ans in 'NnНн' and ans != '':
        break
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    measurement = input('Введите единицы измерения: ')
    row = {'Название': name, 'Цена': price, 'Количество': quantity, 'ед': measurement}
    products.append((i, row))
    i += 1

analit = dict()
for row in products:
    for a, d in row[1].items():
        analit.setdefault(a, []).append(d)

print(analit)
