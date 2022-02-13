class Data:
    def __init__(self, dt):
        self.__data = dt

    @classmethod
    def data_to_num(cls, dt):
        if Data.chek_data(dt):
            return tuple(map(int, dt.split('-')))
        else:
            raise ValueError('Неправильный формат даты. Дата должна быть в формате [dd-mm-yyyy]')

    @staticmethod
    def chek_data(data_str):
        in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        try:
            d, m, y = map(int, data_str.split('-', maxsplit=2))
        except ValueError():
            return False
        if not ((1000 <= y <= 9999)
                and (1 <= m <= 12)
                and (1 <= d <= in_month[m])):
            return False
        return True


data = ['11-02-2025', '35-1-2022', '17-17-2033', '14/17/2027', '24.03.2077', '18-02-2025', '3-7-2022']
for d in data:
    if Data.chek_data(d):
        print(Data.data_to_num(d))
    else:
        print('Ошибка в дате')
