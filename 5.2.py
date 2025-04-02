class Fraction():
    def __init__(self, x, y = None):
        self.check(x, y)
        self.x = x
        if y != None: self.y = y
        else:
            x = round(float(x)*1000, 3)
            y = 1000
            self.x, self.y = self.to_reght_dr(x, y)

        self.value = round(x/y, 3)

    def __add__(self, other):
        if not(isinstance(other, (Fraction))):
            raise AttributeError('Неподходящий тип данных')
        x, y = self.x*other.y + other.x*self.y, self.y*other.y
        x, y = Fraction.to_reght_dr(x, y)

        return (f'{x}/{y}')
        

    def __radd__(self, other):
        return self + other
    

    def __sub__(self, other):
        if not(isinstance(other, (Fraction))):
            raise AttributeError('Неподходящий тип данных')
        x, y = self.x*other.y - other.x*self.y, self.y*other.y
        x, y = Fraction.to_reght_dr(x, y)

        return (f'{x}/{y}')
    

    def __mul__(self, other):
        if not(isinstance(other, (Fraction))):
            raise AttributeError('Неподходящий тип данных')
        x, y = self.x*other.x, self.y*other.y
        x, y = Fraction.to_reght_dr(int(x), int(y))

        return (f'{x}/{y}')


    def __truediv__(self, other):
        if not(isinstance(other, (Fraction))):
            raise AttributeError('Неподходящий тип данных')
        x, y = self.x*other.y, self.y*other.x
        x, y = Fraction.to_reght_dr(x, y)

        return (f'{x}/{y}')


    @staticmethod
    def to_reght_dr(x, y):
        i = 0
        while i != abs(int(y))-1:
            for i in range(abs(int(y))):
                if i != 0 and i != 1 and x/i == x//i and y//i == y/i:
                    x, y = x/i, y/i
                    break
                
        return(int(x), int(y))


    def check(self, x, y):
        if y == 0: raise AttributeError('Zero Devision')
        if y != None and (not(str(x).isdigit()) or not(str(y).isdigit())): raise ArithmeticError('Числа должны быть целыми')
            




# f1 = Fraction(1, 2)
# f2 = Fraction(2.5)
# print(f2.__dict__)
# print(f1 + f2)  # 5/4
# print(f1 - f2)  # -1/4
# print(f1 * f2)  # 3/8
# print(f1 / f2)  # 2/3
# print(f1.value) # 0.5


class FractionMatrix():
    def __init__(self, matr):
        for i in range(len(matr)):
            for j in range(len(matr[i])):
                matr[i][j] = (matr[i][j]).value

        self.matr = matr

    
    def __add__(self, other):
        if type(other) != FractionMatrix: raise AttributeError('Неверный тип данных')

        matr1 = self.matr
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                matr1[i][j] = self.matr[i][j] + other.matr[i][j]
        return matr1
    

    def __mul__(self, other):
        if type(other) != FractionMatrix: raise AttributeError('Неверный тип данных')

        res1 = []
        for i in range(len(self.matr)):
            for n in range(len(self.matr)):
                res = 0
                for j in range(len(self.matr[0])):
                    res += self.matr[i][j] * other.matr[j][n]
                res1.append(res)
        return res1
    

    def transp(self):
        matr1 = self.matr
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                matr1[i][j] = self.matr[j][i]
        return matr1
    
m1 = FractionMatrix([[Fraction(1, 2), Fraction(1, 3)], [Fraction(2, 5), Fraction(3, 4)]])
m2 = FractionMatrix([[Fraction(1, 3), Fraction(2, 3)], [Fraction(1, 2), Fraction(2, 5)]])
    
m1 = FractionMatrix([[Fraction(1), Fraction(2), Fraction(3)], [Fraction(4), Fraction(5), Fraction(6)], [Fraction(7), Fraction(8), Fraction(9)]])
m2 = FractionMatrix([[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]])
print(m1.matr, m2.matr)
print(m1 + m2) 
print(m1 * m2) 
