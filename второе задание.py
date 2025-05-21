import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        if not isinstance(real, (int, float)) or not isinstance(imaginary, (int, float)):
            raise TypeError("Действительная и мнимая части должны быть числами")
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("Можно складывать только комплексные числа")
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("Можно умножать только комплексные числа")
        # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imag_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imag_part)

    def modulus(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def __repr__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {-self.imaginary}i"