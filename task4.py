class Warehouse:
    def __init__(self):
        self.__equipment = {}

    def put(self, eq, count):
        """
        метод "помещает" оборудование на склад
        :param eq: оборудование которое поместили на склад
        :param count: количество оборудования передаваемого на склад
        """
        self.__equipment[eq] = self.__equipment.setdefault(eq, 0) + count

    def get(self, eq, count):
        """
        метод "забирает" оборудование на склад
        :param eq: оборудование которое поместили на склад
        :param count: количество оборудования забираемого со склада
        """
        if not(eq in self.__equipment.keys()) or (self.__equipment[eq] < count):
            return False
        self.__equipment[eq] -= count
        if self.__equipment[eq] == 0:
            del self.__equipment[eq]
        return True

    @property
    def equipment(self):
        return self.__equipment


class OfficeEquipment:
    def __init__(self, type, model):
        self.model = model
        self.type = type

    def __eq__(self, other):
        return (self.type == other.type
                and self.model == other.model)

    def __hash__(self):
        return hash('{self.type}:{self.model}')

    def __repr__(self):
        return f'{self.type}: {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, model, color):
        super().__init__('Принтер', model)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, model, size):
        super().__init__('Сканер', model)
        self.size = size


class Xerox(OfficeEquipment):
    def __init__(self, model):
        super().__init__('Ксерокс', model)


wh = Warehouse()
x1 = Xerox('Xerox 1a')
wh.put(x1, 3)
print(wh.equipment)
x2 = Xerox('Serox 2b')
wh.put(x2, 3)
print(wh.equipment)
x3 = Xerox('Xerox 1a')
wh.put(x3, 3)
print(wh.equipment)
wh.get(x3, 2)
print(wh.equipment)
wh.get(x3, 2)
print(wh.equipment)
p1 = Printer('HP 1100', True)
wh.put(p1, 5)
print(wh.equipment)
s1 = Scanner('Brother Sc1255', 'A4')
wh.put(s1, 10)
print(wh.equipment)
wh.get(Scanner('Brother Sc1255', 'A4'), 4)
print(wh.equipment)
