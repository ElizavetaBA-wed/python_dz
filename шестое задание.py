class Whiteboard:
    def __init__(self):
        self._messages = []

    def add_message(self, msg):
        if not isinstance(msg, str):
            raise TypeError("Сообщение должно быть строкой")
        self._messages.append(msg)

    def __add__(self, other):
        if not isinstance(other, Whiteboard):
            raise TypeError("Можно объединять только с другой доской")
        new_board = Whiteboard()
        new_board._messages = self._messages + other._messages
        return new_board

    def __len__(self):
        return len(self._messages)

    def __call__(self):
        if not self._messages:
            print("Доска пуста")
        else:
            print("Содержимое доски:")
            for i, msg in enumerate(self._messages, 1):
                print(f"{i}. {msg}")

    @property
    def latest_message(self):
        if not self._messages:
            raise ValueError("Нет сообщений на доске")
        return self._messages[-1]

    @latest_message.setter
    def latest_message(self, value):
        if not isinstance(value, str):
            raise TypeError("Сообщение должно быть строкой")
        if not self._messages:
            raise ValueError("Нет сообщений для замены")
        self._messages[-1] = value


# Демонстрация с try-except-finally
try:
    print("Создаем первую доску:")
    board1 = Whiteboard()
    board1.add_message("Первое сообщение")
    board1.add_message("Второе сообщение")
    board1()
    print(f"Количество сообщений: {len(board1)}")
    print(f"Последнее сообщение: {board1.latest_message}")

    print("\nСоздаем вторую доску:")
    board2 = Whiteboard()
    board2.add_message("Третье сообщение")
    board2.add_message("Четвертое сообщение")
    board2()

    print("\nОбъединяем доски:")
    combined = board1 + board2
    combined()
    print(f"Общее количество сообщений: {len(combined)}")

    print("\nИзменяем последнее сообщение:")
    combined.latest_message = "Новое последнее сообщение"
    combined()

    print("\nПроверка обработки ошибок:")
    try:
        board1.add_message(123)  # Не строка
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        bad_combine = board1 + "not a board"  # Не доска
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        empty_board = Whiteboard()
        print(empty_board.latest_message)  # Пустая доска
    except ValueError as e:
        print(f"Ошибка: {e}")

except Exception as e:
    print(f"\nПроизошла непредвиденная ошибка: {e}")
finally:
    print("\nДемонстрация работы с классной доской завершена.")