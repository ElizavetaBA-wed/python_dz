class Student:
    def __init__(self, name, grades):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not isinstance(grades, (list, tuple)):
            raise TypeError("Оценки должны быть списком или кортежем")
        if not all(isinstance(grade, (int, float)) for grade in grades):
            raise TypeError("Все оценки должны быть числами")
        if not grades:
            raise ValueError("Список оценок не может быть пустым")
        
        self.name = name
        self.grades = grades

    def get_grade(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Студент {self.name}, средний балл: {self.get_grade():.2f}"


class MathStudent(Student):
    def get_grade(self):
        # Для математиков учитываем последнюю оценку в 2 раза больше
        if len(self.grades) < 2:
            return super().get_grade()
        
        weighted_grades = self.grades[:-1] + [self.grades[-1] * 2]
        return sum(weighted_grades) / (len(self.grades) + 1)


class HistoryStudent(Student):
    def get_grade(self):
        # Для историков минимальная оценка не учитывается
        if len(self.grades) < 2:
            return super().get_grade()
        
        return (sum(self.grades) - min(self.grades)) / (len(self.grades) - 1)


# Демонстрация полиморфизма
def print_student_grade(student):
    if not isinstance(student, Student):
        raise TypeError("Ожидается объект класса Student")
    print(f"{student.name}: {student.get_grade():.2f}")


# Пример использования
try:
    math_student = MathStudent("Иван", [4, 5, 3, 5])
    history_student = HistoryStudent("Мария", [5, 4, 3, 5])
    base_student = Student("Алексей", [4, 4, 4, 4])

    print(math_student)     # Студент Иван, средний балл: 4.40
    print(history_student)  # Студент Мария, средний балл: 4.67
    print(base_student)     # Студент Алексей, средний балл: 4.00

    # Демонстрация полиморфизма
    print("\nПолиморфизм в действии:")
    for student in [math_student, history_student, base_student]:
        print_student_grade(student)

    # Проверка обработки исключений
    try:
        bad_student = MathStudent(123, [4, 5])  # Неправильное имя
    except TypeError as e:
        print(f"\nОшибка: {e}")

    try:
        bad_student = HistoryStudent("Петр", "5,4,3")  # Оценки не в списке
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        bad_student = Student("Ольга", [])  # Пустой список оценок
    except ValueError as e:
        print(f"Ошибка: {e}")

except Exception as e:
    print(f"Произошла ошибка: {e}")