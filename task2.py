from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name):
        self._name_ = name

    @abstractmethod
    def consumption(self):
        pass

    @property
    def name(self):
        return self._name_

class Coat(Clothes):
    def __init__(self, name, vol):
        super().__init__(name)
        self.v = vol

    @property
    def consumption(self):
        return round(self.v / 6.5 + 0.5, 3)


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.h = height

    @property
    def consumption(self):
        return round(self.h * 2 + 0.3, 3)

cl = Coat('Шикардос', 10)
print(f'Расход ткани для {cl.name} - {cl.consumption} v2')

st = Suit('Официал', 5)
print(f'Расход ткани для {st.name} - {st.consumption} м2')