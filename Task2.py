def info(first_name, second_name, year, city, mail, phone):
    """
    Формирует строку с данными о персоне
    :param first_name:
    :param second_name:
    :param year:
    :param city:
    :param mail:
    :param phone:
    :return: string
    """
    result = f'{second_name} {first_name}, {year} года рождения. \nПроживает в {city}\n' \
             f'e-mail: {mail} \nТелефон: {phone}'
    return result

print(info('Максим', 'Михеев', 2000, "Тверь-сити", 'maksim@mail.ru', '+7 910 322 22 11'))

