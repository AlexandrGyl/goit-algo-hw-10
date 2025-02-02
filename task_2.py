import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x**2+5

def monte_carlo_integral(func, a, b, num_points):
    x_random = np.random.uniform(a, b, num_points)
    f_values = func(x_random)
    avg_value = np.mean(f_values)
    
    area = b - a
     
    integral_estimate = avg_value * area
    return integral_estimate

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
ax.set_title('Графік інтегрування f(x) = x^2+5 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

result, error = spi.quad(f, a, b)

num_points = 1000000  # Кількість випадкових точок
monte_carlo_result = monte_carlo_integral(f, a, b, num_points)

# Виведення результатів
print(f"Інтеграл (метод Монте-Карло): {monte_carlo_result}")
print(f"Інтеграл (стандартний метод): {result}, Похибка: {error}")