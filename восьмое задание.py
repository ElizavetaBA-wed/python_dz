from abc import ABC, abstractmethod

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Имя должно быть строкой")
        if len(value) < 2:
            raise ValueError("Имя слишком короткое")
        self._name = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email должен быть строкой")
        if "@" not in value:
            raise ValueError("Некорректный email")
        self._email = value
    
    def __str__(self):
        return f"Клиент: {self.name} ({self.email})"


class LoggedEntity(ABC):
    def __init__(self):
        self._log = []
    
    @property
    def log(self):
        return self._log.copy()
    
    def add_log_entry(self, message):
        if not isinstance(message, str):
            raise TypeError("Запись лога должна быть строкой")
        self._log.append(message)
    
    @abstractmethod
    def __str__(self):
        pass


class Order:
    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Неверный тип клиента")
        self._customer = customer
        self._items = []
        self._prices = []
    
    @property
    def customer(self):
        return self._customer
    
    def add_item(self, item, price):
        if not isinstance(item, str):
            raise TypeError("Название товара должно быть строкой")
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом")
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        
        self._items.append(item)
        self._prices.append(price)
    
    def get_total(self):
        if not self._items:
            raise ValueError("Заказ пуст")
        try:
            return sum(self._prices)
        except Exception as e:
            raise RuntimeError(f"Ошибка расчета суммы: {e}")
    
    def __str__(self):
        if not self._items:
            return f"Заказ клиента {self.customer.name} (пуст)"
        
        items_str = "\n".join(f"  - {item}: {price:.2f} руб." 
                            for item, price in zip(self._items, self._prices))
        return (f"Заказ клиента {self.customer.name}:\n"
                f"{items_str}\n"
                f"Итого: {self.get_total():.2f} руб.")


class OrderWithLogging(Order, LoggedEntity):
    def __init__(self, customer):
        Order.__init__(self, customer)
        LoggedEntity.__init__(self)
        self.add_log_entry("Создан новый заказ")
    
    def add_item(self, item, price):
        try:
            super().add_item(item, price)
            self.add_log_entry(f"Добавлен товар: {item} за {price:.2f} руб.")
        except Exception as e:
            self.add_log_entry(f"Ошибка добавления товара: {str(e)}")
            raise
    
    def get_total(self):
        try:
            total = super().get_total()
            self.add_log_entry(f"Запрошена сумма заказа: {total:.2f} руб.")
            return total
        except Exception as e:
            self.add_log_entry(f"Ошибка расчета суммы: {str(e)}")
            raise
    
    def __str__(self):
        order_str = Order.__str__(self)
        log_str = "\n".join(f"[LOG] {entry}" for entry in self.log[-3:])  # Последние 3 записи
        return f"{order_str}\n\nЛог:\n{log_str}"


# Демонстрационный блок с try-except-finally
try:
    print("Создаем клиента:")
    customer = Customer("Иван Иванов", "ivan@example.com")
    print(customer)

    print("\nСоздаем заказ с логированием:")
    order = OrderWithLogging(customer)
    
    print("\nДобавляем товары:")
    order.add_item("Ноутбук", 75000)
    order.add_item("Мышь", 1500)
    order.add_item("Клавиатура", 3000)
    
    print("\nИнформация о заказе:")
    print(order)
    
    print("\nПолучаем сумму заказа:")
    total = order.get_total()
    print(f"Общая сумма: {total:.2f} руб.")

    print("\nПроверка обработки ошибок:")
    try:
        order.add_item("", 100)  # Пустое название
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        order.add_item("Наушники", -500)  # Отрицательная цена
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        empty_order = OrderWithLogging(customer)
        print(empty_order.get_total())  # Пустой заказ
    except ValueError as e:
        print(f"Ошибка: {e}")

except Exception as e:
    print(f"\nПроизошла непредвиденная ошибка: {e}")
finally:
    print("\nДемонстрация системы заказов завершена.")