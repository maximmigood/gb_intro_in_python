n = int(input('Введите целое положительное число: '))
current_max_dig = 0
while n>0:
    dig = n % 10
    if dig > current_max_dig:
        current_max_dig = dig
    n //= 10
print('Наибольшая цифра во введённом числе -', current_max_dig)
