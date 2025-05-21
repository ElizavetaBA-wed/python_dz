class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius  # Используем сеттер для валидации

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Температура должна быть числом")
        self._celsius = value

    @property
    def fahrenheit(self):
        # Формула: F = C * 9/5 + 32
        try:
            return self._celsius * 9/5 + 32
        except ZeroDivisionError:
            raise ValueError("Ошибка при конвертации температуры")

    @fahrenheit.setter
    def fahrenheit(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Температура должна быть числом")
        try:
            # Формула: C = (F - 32) * 5/9
            self._celsius = (value - 32) * 5/9
        except ZeroDivisionError:
            raise ValueError("Ошибка при конвертации температуры")

    def __str__(self):
        return f"{self._celsius:.1f}°C ({self.fahrenheit:.1f}°F)"


# Пример использования
try:
    t1 = Temperature(25)
    print(t1)  # 25.0°C (77.0°F)

    t2 = Temperature()
    t2.fahrenheit = 32  # Установка температуры через Фаренгейты
    print(t2)  # 0.0°C (32.0°F)

    t3 = Temperature(-40)
    print(t3)  # -40.0°C (-40.0°F)

    # Проверка обработки ошибок
    try:
        t4 = Temperature("100")  # Неправильный тип
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        t5 = Temperature(100)
        t5.fahrenheit = "50"  # Неправильный тип
    except TypeError as e:
        print(f"Ошибка: {e}")

except Exception as e:
    print(f"Произошла ошибка: {e}")