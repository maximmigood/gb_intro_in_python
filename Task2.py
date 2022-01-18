tm = int(input('Введите время в секундах: '))
hours = tm // (60 * 60)
minutes = (tm % 3600) // 60
seconds = tm % 60
print(f'{hours}:{minutes}:{seconds}')
