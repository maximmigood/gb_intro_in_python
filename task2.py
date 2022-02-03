with open('task2.txt') as file_obj:
    f = file_obj.readlines()
print(f'В файле {len(f)} строк')
words = 0
for s in f:
    words += len(s.split())
print(f'В файле {words} слов')
