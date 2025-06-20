import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Визначення змінних
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")         # Кількість "Лимонаду"
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")   # Кількість "Фруктового соку"

# Функція цілі: максимізація загальної кількості вироблених напоїв
model += lemonade + fruit_juice, "Total"

# Обмеження на ресурси
model += (2 * lemonade + fruit_juice <= 100) # Вода
model += (lemonade <= 50) # Цукор
model += (lemonade <= 30) # Лимонний сік
model += (2 * fruit_juice <= 40)  # Фруктове пюре

# Розв'язання задачі
model.solve()

# Вивід результатів
print(f"Оптимальна кількість Лимонаду: {lemonade.varValue}")
print(f"Оптимальна кількість Фруктового соку: {fruit_juice.varValue}")