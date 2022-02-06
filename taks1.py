class TrafficLight:
    __colors = {"Красный": [7, "Жёлтый"],
                "Жёлтый":  [2, "Зелёный"],
                "Зелёный": [10, "Красный"]}

    def __init__(self, start_color):
        if start_color in TrafficLight.__colors.keys():
            self.__color = start_color
        else:
            self.__color = "Красный"
            print(f"У светофора нет цвета {start_color}. Задан 'Красный' цвет")

    def running(self):
        print(f'{self.__color} горит {self.__colors[self.__color][0]} сек.')
        self.__color = self.__colors[self.__color][1]


tl = TrafficLight('Зеленый')

tl.running()
tl.running()
tl.running()
tl.running()
