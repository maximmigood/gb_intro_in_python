from itertools import count, cycle


def gen1(n):
    """
    Генератор целых числе. Возвращает 7 значений
    :param n: стартовое число
    """
    i = n
    while True:
        if i <= n + 7:
            yield i
        else:
            return
        i += 1


def gen1_2(n):
    """
    Генератор целых чисел. Возвращает 13 чисел
    :param n: стартовое число
    """
    for el in count(n):
        if el <= n + 13:
            yield el
        else:
            break


def gen2(ls):
    """
    Генератор значений из списка. возвращет 30 элементов
    :param ls: исходный список для генератора
    :return:
    """
    z = cycle(ls)
    for _ in range(30):
        yield next(z)


def check_gen(gen):
    print(gen)
    for el in gen:
        print(el)


print('-- Проверяем генератор 1 (7 повторений)--')
check_gen(gen1(5))

print('-- Проверяем генератор 1_2 (13 повторений)--')
check_gen(gen1_2(20))

print('-- Проверяем генератор 2 (30 повторений)--')
check_gen(gen2([20, 30, 2, 3]))
