sum = 0
end_input = "z"
def sum_str(str):
    """
    Добавляет в глобальную переменную sum сумму чисел из переданной строки
    :param str:
    :return: Boolean
    """
    global sum
    l = str.split()
    k = l.index(end_input) if end_input in l else len(l)
    for i in range(k):
        sum += int(l[i])
    return len(l) == k


cont = True
while cont:
    cont = sum_str(input('Введите строку с числами разделённые пробелами: '))
    print(sum)
