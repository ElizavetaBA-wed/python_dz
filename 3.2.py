class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    @staticmethod
    def cheak_year(cls, year):
        if year.isinstance:
            return True
    
    @classmethod
    def create_default_year(cls,__title, __author):
        cls.__year = 2025
        return cls(__title, __author, cls.__year)
    
    def get_info(self):
        print(f"{self.__title}, автор: {self.__author}")


book1 = Book("1984", "George Orwell", 1949)
print(book1.get_info())  # Вывод: "1984, автор: George Orwell, год: 1949"

book2 = Book.create_default_year("Brave New World", "Aldous Huxley")
print(book2.get_info())  # Вывод: "Brave New World, автор: Aldous Huxley, год: 2024"