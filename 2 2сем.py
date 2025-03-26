class Recipe():

    def __init__(self, dish, ingredients : str):
        self.dish = dish
        self.ingredients = ingredients


    def print_ingredients(self):
        print(self.ingredients, sep = "\n")
        for i in self.ingredients: 
            print(f"- {i}")


    def cook(self):
        print(f"Сегодня мы готовим {self.dish}.")
        print(f"Выполняем инструкцию по приготовлению блюда {self.dish}...",) 
        print(f"Блюдо {self.dish} готово!")

spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])

# печатаем список продуктов для рецепта спагетти
spaghetti.print_ingredients()

# готовим спагетти
spaghetti.cook()

# создаем рецепт для кекса
cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])

# печатаем рецепт кекса
cake.print_ingredients()

# готовим кекс
cake.cook()

