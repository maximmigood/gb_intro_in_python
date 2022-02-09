a = float(input('Введите число: '))
b = int(input('Введите отрицательное целое число: '))


def my_func(x, y):
    return x ** y


def my_func_(x, y):
    """
    Функция возведения x в степень y
    :param x:
    :param y:
    :return:
    """
    res = 1
    for _ in range(-y):
        res *= x
    return 1 / res


print(f'Функция my_func({a}, {b}) возвращает {my_func(a, b)})
print()
print(f'Функция my_func({a}, {b}) возвращает {my_func_(a, b)})