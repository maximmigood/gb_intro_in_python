def int_func(w):
    """
    Переводит в верхний регистр первую букву слова
    :param w: str
    :return: str
    """
    return w[0].upper() + w[1:]


def long_int_func(s):
    """
    Переводит в верхний регистр все слова предложения
    :param s: str
    :return: str
    """
    l = []
    for w in s.split():
        l.append(int_func(w))
    return ' '.join(l)

print(long_int_func('brown fox jumps over the lazy dog'))

