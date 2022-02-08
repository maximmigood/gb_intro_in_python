class Car:
    def __init__(self, max_speed, color, name, is_police=False):
        self.max_speed = max_speed
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        if speed > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed = speed
        print(f'Едем. Скорость {self.speed}км/ч')

    def stop(self):
        print('Остановились')

    def turn(self, direction):
        print(f'Поворот на {direction} градусов')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превышаете ограничение скорости в 60км/ч. Ваша скорость {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превышаете ограничение скорости в 40 км/ч. Ваша скорость {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


cars = [WorkCar(60, 'Оранжевый', 'Камаз'),
        PoliceCar(150, 'Белый', 'Ford'),
        TownCar(120, 'Серая', 'Lada Vesta'),
        SportCar(200, 'Красная', 'Феррари', True)]


for i, car in enumerate(cars):
    print(f'----- {car.color} {car.name} {car.show_speed()} -----')
    car.go(30)
    car.show_speed()
    car.go(50)
    car.show_speed()
    car.turn(80)
    car.go(90)
    car.show_speed()
    car.go(50)
    car.show_speed()
    car.go(10)
    car.show_speed()
    car.stop()
