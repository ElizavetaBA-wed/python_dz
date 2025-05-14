class Animal:
    def sound(self):
        return ""  # Пустая строка как поведение по умолчанию

class Dog(Animal):
    def sound(self):
        return "Гав-гав"

class Cat(Animal):
    def sound(self):
        return "Мяу"

class Cow(Animal):
    def sound(self):
        return "Муу"

# Пример использования
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.sound())