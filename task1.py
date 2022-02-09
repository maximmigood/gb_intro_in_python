class Matrix:
    def __init__(self, m):
        self.mtr = m

    def __str__(self):
        res = ''.join([str(a)+'\n' for a in self.mtr])
        return res

    def __add__(self, m2):
        res = [[self.mtr[i][j] + m2[i][j] for j in range(len(self.mtr[i]))] for i in range(len(self.mtr))]
        return Matrix(res)

ma = Matrix([[1, 2], [4, 5]])
ma2 = Matrix([[2, 2], [3, 3]])
print(ma + ma2)