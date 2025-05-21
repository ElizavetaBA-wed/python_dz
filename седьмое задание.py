class Function:
    def __call__(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Аргумент x должен быть числом")
        return self._calculate(x)
    
    def _calculate(self, x):
        raise NotImplementedError("Метод должен быть переопределен в подклассах")
    
    def __repr__(self):
        return "Базовый класс функции"
    
    def __eq__(self, other):
        if not isinstance(other, Function):
            return NotImplemented
        return self(1) == other(1)
    
    def __lt__(self, other):
        if not isinstance(other, Function):
            return NotImplemented
        return self(1) < other(1)


class LinearFunction(Function):
    def __init__(self, a, b):
        if not all(isinstance(coef, (int, float)) for coef in [a, b]):
            raise TypeError("Коэффициенты должны быть числами")
        self.a = a
        self.b = b
    
    def _calculate(self, x):
        return self.a * x + self.b
    
    def __repr__(self):
        return f"Линейная функция: {self.a}x + {self.b}"


class QuadraticFunction(Function):
    def __init__(self, a, b, c):
        if not all(isinstance(coef, (int, float)) for coef in [a, b, c]):
            raise TypeError("Коэффициенты должны быть числами")
        self.a = a
        self.b = b
        self.c = c
    
    def _calculate(self, x):
        return self.a * x**2 + self.b * x + self.c
    
    def __repr__(self):
        return f"Квадратичная функция: {self.a}x² + {self.b}x + {self.c}"


# Демонстрация с try-except-finally
try:
    print("Создаем функции:")
    f1 = LinearFunction(2, 3)
    f2 = QuadraticFunction(1, -2, 1)
    print(f1)  # Линейная функция: 2x + 3
    print(f2)  # Квадратичная функция: 1x² + -2x + 1

    print("\nВычисляем значения:")
    x = 2
    print(f"f1({x}) = {f1(x)}")  # 2*2 + 3 = 7
    print(f"f2({x}) = {f2(x)}")  # 1*4 + -2*2 + 1 = 1

    print("\nСравниваем функции в точке x=1:")
    print(f"f1(1) = {f1(1)}, f2(1) = {f2(1)}")
    print(f"f1 == f2: {f1 == f2}")  # 5 == 0 → False
    print(f"f1 < f2: {f1 < f2}")     # 5 < 0 → False
    print(f"f1 > f2: {f1 > f2}")     # 5 > 0 → True

    print("\nПроверка обработки ошибок:")
    try:
        bad_linear = LinearFunction("2", 3)  # Не число
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        print(f1("text"))  # Неправильный тип аргумента
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        print(f1 == "not a function")  # Сравнение с не-функцией
    except TypeError as e:
        print(f"Ошибка: {e}")

except Exception as e:
    print(f"\nПроизошла непредвиденная ошибка: {e}")
finally:
    print("\nДемонстрация работы с функциями завершена.")