a = float(input('Введите число: '))
b = int(input('Введите отрицательное целое число: '))

my_func = lambda x, y: x ** y

def my_func_(x, y):
    """
    Функция возведения x в степень y
    :param x:
    :param y:
    :return:
    """
    return x ** y

print(my_func(a, b))
