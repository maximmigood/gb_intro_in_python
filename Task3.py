def my_func(num1, num2, num3):
    """
    Функция возвращает сумму двух наибольших аргументов
    :param num1: параметр №1
    :param num2: параметр №2
    :param num3: параметр №2
    :return:
    """
    return num1 + num2 + num3 - min(num1, num2, num3)


print(my_func(25, 17, 23))
