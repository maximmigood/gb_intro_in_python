class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print('Изображение ручки')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print('Изображение карандаша')


class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print('Изображение маркера')


stationeries = [
    Stationery('Степлер'),
    Pen(),
    Pencil(),
    Handle()
]

for s in stationeries:
    s.draw()
