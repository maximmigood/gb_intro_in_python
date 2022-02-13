class NotNumInList(ValueError):
    def __init__(self, message):
        self.txt = message
    pass


class MyList(list):
    def append_num_in_list(self, data):
        if type(data) == int or type(data) == float:
            self.append(data)
            return
        if type(data) == str:
            try:
                num = int(data)
            except ValueError:
                try:
                    num = float(data)
                except ValueError:
                    raise NotNumInList(f"{data} - can't convert to number.")
            self.append(num)
        else:
            raise NotNumInList(f"{data} - is not number. It's {type(data)}")


my_lst = MyList()

a = input('Введите число: ')
while a != 'stop':
    try:
        my_lst.append_num_in_list(a)
    except NotNumInList as err:
        print(err.txt)
    a = input('Введите число: ')

# добавляем в список данные типа int и float
my_lst.append_num_in_list(66)
my_lst.append_num_in_list(38.7)
print(my_lst)

print('------ попробуем добавить в my_list список-----')
try:
    my_lst.append_num_in_list(['45', 77])
except ValueError:
    print('Добавить список в my_list не получилось')
