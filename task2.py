class DivisionByZerro(Exception):
    def __init__(self, txt=''):
        if txt:
            self.txt = txt
        else:
            self.txt = 'Деление на 0 запрещено.'

def div(a, b):
    if b == 0:
        raise DivisionByZerro()
    else:
        return a / b


while True:
    s = input('Введите два числа разделённых пробелом (делимое и делитель):')
    if s:
        try:
            a, b = map(int, s.split())
        except ValueError as err:
            print('Необходимо ввести только 2 числа разделённых пробелом. Повторите ввод.')
            continue
    else:
        break
    try:
        print(f'{div(a, b):.3f}')
    except DivisionByZerro as err:
        print(f'{err.txt} Повторите ввод')

