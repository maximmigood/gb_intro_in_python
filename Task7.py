import math
def trans(n):

first_day = float(input('Расстояние, которое пробежали за первый день: '))
result = float(input('Расстояние которое хотите пробегать: '))
current_distance = first_day
current_day = 1
while current_distance < result:
    current_day += 1
    current_distance *= 1.1
print(f'На {current_day} день спортсмен достиг результата - не менее {result} км')
print(f'На {(math.log(result / first_day, 1.1)+1.5):.0f} день спортсмен достиг результата - не менее {result} км')