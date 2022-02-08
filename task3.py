class Worker:
    """
    Реализация базового класса Worker
    """
    def __init__(self, name, surename, position, wage, bonus):
        self.name = name
        self.surename = surename
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surename}'

    def get_total_income(self):
        return self.income['wage'] + self.income['bonus']


persons = [Position('Иван', "Иванов", "Консультант", 10000, 30000),  # создаём экземпляр, передаём данные
           Position("Петр", "Петров", "Главный консультант", 13000, 50000)]  # создаём экземпляр, передаём данные
print('------------------------')
for p in persons:
    print(f'У сотрудника {p.get_full_name()} \n'  # вызываем методы экземпляра
          f'работющего на должности {p.position}\n'  # проверяем значения атрибутов
          f'ежемесячный доход составляет до {p.get_total_income()} рублей')  # вызываем методы экземпляра
    print('----------------------------')
