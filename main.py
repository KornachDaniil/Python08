import numpy as np
import matplotlib.pyplot as plt


# Функция, которую мы интегрируем
def f(x):
    return np.sin(x) * np.cos(x)


# Аналитическое решение
analytical_solution = 0.5


# Метод Монте-Карло
def monte_carlo_integration(func, a, b, num_samples):
    x = np.random.uniform(a, b, num_samples)
    y = np.random.uniform(0, 1, num_samples)
    count_inside = np.sum(y <= func(x))
    return (count_inside / num_samples) * (b - a)


# Границы интегрирования
a = 0
b = np.pi / 2

# Количество испытаний
num_samples_list = [10, 100, 1000, 10000, 100000]

# Проводим интегрирование методом Монте-Карло для разного количества испытаний
monte_carlo_results = []
for num_samples in num_samples_list:
    result = monte_carlo_integration(f, a, b, num_samples)
    monte_carlo_results.append(result)

# Вычисляем ошибки интегрирования
errors = np.abs(np.array(monte_carlo_results) - analytical_solution)

# Построение графиков
plt.figure(figsize=(14, 5))

# График функции
plt.subplot(1, 2, 1)
x_values = np.linspace(a, b, 1000)
plt.plot(x_values, f(x_values), color='blue', label='$\sin(x) \cos(x)$')
plt.fill_between(x_values, f(x_values), color='lightblue')
plt.xlabel('$x$')
plt.ylabel('$\sin(x) \cos(x)$')
plt.title('График функции')
plt.legend()

# График зависимости ошибок интегрирования от числа испытаний
plt.subplot(1, 2, 2)
plt.plot(num_samples_list, errors, marker='o', color='red')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Число испытаний')
plt.ylabel('Ошибка')
plt.title('Зависимость ошибок интегрирования')
plt.grid(True)

plt.tight_layout()
plt.show()
