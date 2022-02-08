class Road:
    def __init__(self, width, length):
        self.__length = length
        self.__width = width

    def calculate_mass(self, mass, thikness):
        return self.__width * self.__length * thikness * mass


r = Road(20, 5000)
print(f'{r.calculate_mass(25, 5):n}')
