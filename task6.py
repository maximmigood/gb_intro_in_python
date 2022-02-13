class Warehouse:
    def __init__(self, name):
        self.__equipment = {}
        self.name = name

    def put(self, eq, count):
        """
        метод "помещает" оборудование на склад
        :param eq: оборудование которое поместили на склад
        :param count: количество оборудования передаваемого на склад
        """
        if isinstance(eq, OfficeEquipment) and type(count) == int:
            self.__equipment[eq] = self.__equipment.setdefault(eq, 0) + count
        else:
            if not isinstance(eq, OfficeEquipment):
                raise TypeError('Parametr 1 [eq] must be OfficeEquipment')
            if not (type(count) == int):
                raise TypeError('Parametr 2 [count] must be int')

    def get(self, eq, count):
        """
        метод "забирает" оборудование на склад
        :param eq: оборудование которое поместили на склад
        :param count: количество оборудования забираемого со склада
        """
        if isinstance(eq, OfficeEquipment) and type(count) == int:
            if not(eq in self.__equipment.keys()) or (self.__equipment[eq] < count):
                return False
            self.__equipment[eq] -= count
            if self.__equipment[eq] == 0:
                del self.__equipment[eq]
            return True
        else:
            if not isinstance(eq, OfficeEquipment):
                raise TypeError('Parametr 1 [eq] must be OfficeEquipment')
            if not (type(count) == int):
                raise TypeError('Parametr 2 [count] must be int')

    def transfer_to(self, eq, count, to):
        """
        метод "забирает" оборудование на склад
        :param eq: оборудование которое поместили на склад
        :param count: количество оборудования забираемого со склада
        :param to: подразделение куда передётся оборудование
        """
        if (isinstance(eq, OfficeEquipment)
                and type(count) == int
                and isinstance(to, Warehouse)):
            if self.get(eq, count):
                to.put(eq, count)
                return True
            else:
                return False
        else:
            if not isinstance(eq, OfficeEquipment):
                raise TypeError('Parametr 1 [eq] must be OfficeEquipment')
            if not (type(count) == int):
                raise TypeError('Parametr 2 [count] must be int')
            if not isinstance(eq, Warehouse):
                raise TypeError('Parametr 3 [to] must be Warehouse')

    @property
    def equipment(self):
        return self.__equipment

    def __repr__(self):
        return f'{self.name}: [{self.__equipment}]'

class OfficeEquipment:
    def __init__(self, tp, model):
        if not (type(model) == str):
            raise TypeError('Parametr 1 [type] must be str')
        if not (type(tp) == str):
            raise TypeError('Parametr 2 [model] must be str')
        self.model = model
        self.type = tp

    def __eq__(self, other):
        return (self.type == other.type
                and self.model == other.model)

    def __hash__(self):
        return hash('{self.type}:{self.model}')

    def __repr__(self):
        return f'{self.type}: {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, model, color=False):
        if not type(model) == str:
            raise TypeError('Parametr 1 [type] must be str')
        if not type(color) == bool:
            raise TypeError('Parametr 2 [color] must be bool')
        super().__init__('Принтер', model)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, model, size='A4'):
        if not type(model) == str:
            raise TypeError('Parametr 1 [type] must be str')
        if not type(size) == str:
            raise TypeError('Parametr 2 [size] must be str')
        super().__init__('Сканер', model)
        self.size = size


class Xerox(OfficeEquipment):
    def __init__(self, model):
        if not type(model) == str:
            raise TypeError('Parametr 1 [type] must be str')
        super().__init__('Ксерокс', model)


wh = Warehouse('Общий склад')
wh_ec = Warehouse('Электроцех')
wh_b = Warehouse('Бухгалтерия')
print(wh)
print(wh_ec)
print(wh_b)

sc1 = Scanner('Brother S14')
#sc2 = Scanner(14) # Вызывает ошибку
wh.put(Xerox('Xerox Z25-12'), 10)
#wh.put(Xerox('Xerox Z25-12'), '42') # Вызывает ошибку
#wh.put('Xerox Z25-12', 10) # Вызывает ошибку
wh.put(Printer('HP WhideColor 1785H', True), 5)
wh.put(sc1, 2)
print(wh)
print(wh_ec)
print(wh_b)

wh.transfer_to(Xerox('Xerox Z25-12'), 3, wh_ec)
wh.transfer_to(sc1, 1, wh_b)
print(wh)
print(wh_ec)
print(wh_b)

wh.transfer_to(sc1, 1, wh_b)
print(wh)
print(wh_ec)
print(wh_b)


