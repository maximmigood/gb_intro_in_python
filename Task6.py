revenue = int(input('Введите выручку фирмы за год: '))
costs = int(input('Введите издержки фирмы за год: '))
if revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue
    print(f'Рентабельность выручки (прибыль/выручку) - {profitability:.2f}')
    num_employees = int(input('Введите количество сотрудников в фирме: '))
    profit_per_employee = profit / num_employees
    print(f'Прибыль фирмы на одного сотрудника составляет {profit_per_employee:.2f}')
