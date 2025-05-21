class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой")
        if len(value) < 2:
            raise ValueError("Название слишком короткое")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом")
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value

    def get_discounted_price(self, discount):
        try:
            if not isinstance(discount, (int, float)):
                raise TypeError("Скидка должна быть числом")
            if discount < 0:
                raise ValueError("Скидка не может быть отрицательной")
            if discount >= 100:
                raise ValueError("Скидка не может быть 100% и более")
            
            return self.price * (100 - discount) / 100
        except ZeroDivisionError:
            raise ValueError("Ошибка расчета скидки (деление на ноль)")
        except Exception as e:
            raise e

    def __str__(self):
        return f"{self.name} - {self.price:.2f} руб."


class Book(Product):
    def __init__(self, name, price, author, pages):
        super().__init__(name, price)
        self.author = author
        self.pages = pages

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("Автор должен быть строкой")
        if len(value) < 2:
            raise ValueError("Имя автора слишком короткое")
        self._author = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __str__(self):
        return (f"Книга: {self.name}, автор: {self.author}, "
                f"{self.pages} стр., цена: {self.price:.2f} руб.")


class EBook(Book):
    def __init__(self, name, price, author, pages, file_size, file_format):
        super().__init__(name, price, author, pages)
        self.file_size = file_size
        self.file_format = file_format

    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Размер файла должен быть числом")
        if value <= 0:
            raise ValueError("Размер файла должен быть положительным")
        self._file_size = value

    @property
    def file_format(self):
        return self._file_format

    @file_format.setter
    def file_format(self, value):
        if not isinstance(value, str):
            raise TypeError("Формат файла должен быть строкой")
        if value.lower() not in ['pdf', 'epub', 'fb2', 'mobi']:
            raise ValueError("Неподдерживаемый формат файла")
        self._file_format = value.lower()

    def __str__(self):
        return (f"Электронная книга: {self.name}, автор: {self.author}, "
                f"формат: {self.file_format}, {self.file_size:.1f} MB, "
                f"цена: {self.price:.2f} руб.")


# Демонстрационный блок с try-except-finally
try:
    print("\nСоздаем обычную книгу:")
    book = Book("Война и мир", 1200, "Лев Толстой", 1300)
    print(book)
    print(f"Цена со скидкой 20%: {book.get_discounted_price(20):.2f} руб.")

    print("\nСоздаем электронную книгу:")
    ebook = EBook("1984", 500, "Джордж Оруэлл", 328, 2.5, "epub")
    print(ebook)
    print(f"Цена со скидкой 15%: {ebook.get_discounted_price(15):.2f} руб.")

    print("\nПроверка обработки ошибок:")
    try:
        bad_book = Book("А", 100, "Б", 10)  # Слишком короткое название
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        bad_ebook = EBook("О дивный новый мир", -100, "Олдос Хаксли", 288, 3.2, "txt")
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        print(book.get_discounted_price(120))  # Слишком большая скидка
    except ValueError as e:
        print(f"Ошибка: {e}")

except Exception as e:
    print(f"\nПроизошла непредвиденная ошибка: {e}")
finally:
    print("\nДемонстрация завершена. Проверьте результаты выше.")