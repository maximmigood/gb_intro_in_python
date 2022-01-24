def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return f'Вы пытаетесь делить {num1} на 0. Деление на 0 невозможно.'



print(division(3, 5))
print(division(4, 0))
print(division(2, 1))
