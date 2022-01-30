from sys import argv


error_message = f""" Недостаточно параметров
 вызовите task1.py в виде 
 task1.py parametr1 parametr2 parametr3
   parametr1 - выработка в часах (int)
   parametr2 - ставка в час (float)
   parametr3 - премия"""
if len(argv) < 4:
    print(error_message)
    exit(1)

script_name, time, rate, bonus = argv
time = int(time)
rate = float(rate)
bonus = int(bonus)

print(f'Заработок составит {time * rate + bonus}')
