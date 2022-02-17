class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if (self.cells - other.cells) > 0:
            return Cell(self.cells - other.cells)
        else:
            print(f'Нельзя вычитать из клетки с {min(self.cells, other.cells)}'
                  f' ячейками клетку с {max(self.cells, other.cells)} ячпейками')
            return

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, in_row):
        return ('*' * in_row + '\n') * (self.cells // in_row) + '*' * (self.cells % in_row)


c1 = Cell(11)
c2 = Cell(6)
print(c1.make_order(5))
print('-' * 20)

c3 = c1 + c2
print(c3.make_order(5))
print('-' * 20)

c3 = c1 - c2
print(c3.make_order(5))
print('-' * 20)

c3 = c2 - c1
print(c3.make_order(5))
print('-' * 20)


c3 = c1 * c2
print(c3.make_order(5))
print('-' * 20)

c3 = c1 / c2
print(c3.make_order(5))
print('-' * 20)
