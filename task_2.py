import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi
# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Кількість випадкових точок
N = 1000

# Генерація випадкових точок у прямокутнику 
points = [(random.uniform(a, b), random.uniform(0, f(b))) for _ in range(N)]

# Відбір точок, що знаходяться під кривою
inside_points = [point for point in points if point[1] <= f(point[0])]

# Обчислення площі методом Монте-Карло
rect = (b - a) * f(b)  # Площа прямокутника
monte_carlo = (len(inside_points) / N) * rect

# Обчислення інтеграла за допомогою quad
result, error = spi.quad(f, a, b)

print(f'Кількість випадкових точок: {N}')
print(f'Наближене значення (Монте-Карло): {monte_carlo:.4f}')
print("Інтеграл (функція quad): ", result, error)