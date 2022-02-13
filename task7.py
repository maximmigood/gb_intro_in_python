class MyComplex:
    def __init__(self, re, im):
        if type(re) in (int, float) and type(im) in (int, float):
            self.__re = re
            self.__im = im
        else:
            raise TypeError('Both parth of MyComplex must be number')

    def __add__(self, other):
        if isinstance(other, MyComplex):
            return MyComplex(self.__re + other.re, self.__im + other.im)
        else:
            raise TypeError('Second term must be MyComplex')

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            return MyComplex(self.__re * other.re - self.__im * other.im, self.__re * other.im + self.__im * other.re)
        else:
            raise TypeError('Second term must be MyComplex')

    def __repr__(self):
        return f'({self.__re}+{self.__im}i)'

    @property
    def re(self):
        return self.__re

    @property
    def im(self):
        return self.__im

print('------ MyComplex ---------')
a = MyComplex(3, 4)
b = MyComplex(1, 1)
print(f'{a=}      {b=}')
print(f'{a + b=}')
print(f'{a * b=}')

print('------ complex -----------')
aa = complex(3, 4)
bb = complex(1, 1)
print(f'{aa=}      {bb=}')
print(f'{aa + bb=}')
print(f'{aa * bb=}')