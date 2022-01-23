products = []
# Собираем данные
i = 1
while True:
    ans = input('Будете вводить данные о товаре? (N(nНн) - Выход): ')
    if ans in 'NnНн' and ans != '':
        break
    name = input('Введите название товара: ')
    price = input('Введите цену товара: ')
    quantity = input('Введите количество товара: ')
    measurement = input('Введите единицы измерения: ')
    row = {'name': name, 'price': price, 'quant': quantity, 'measure': measurement}
    products.append((i, row))
    i += 1

analit = dict()
for el in products[0]:
    analit[el] = []

print(analit)

# Собираем аналитику
