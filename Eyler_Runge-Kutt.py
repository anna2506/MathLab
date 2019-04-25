from math import exp
import matplotlib.pyplot as plt


def derivative(x, y):
    return (y**3*exp(-x) - y)/x


a, b, y1 = 1, 2, 1
x_new, y_new, x, y, y_der, y_kut = [], [], [], [], [], []
step = (b - a)/float(100)
add = a
x_new.append(add)
y_new.append(y1)
y_kut.append(y1)
y_der.append(derivative(add, y1))
y.append(y1)
x.append(a)
#Метод Эйлера
for i in range(1, 100):
    if i % 10 == 0:
        x.append(add)
        y.append(y1)
    y1 = y_new[i - 1] + step*derivative(add, y1)
    add += step
    #y_der.append(derivative(add, y1))
    x_new.append(add)
    y_new.append(y1)
    # Метод Рунге-Кутта
    y_rung = y_kut[i - 1] + step*derivative(x_new[i - 1], y_kut[i - 1])
    y_kut.append(y_kut[i - 1] + step/2*(derivative(x_new[i - 1], y_kut[i - 1]) + derivative(x_new[i], y_rung)))
print(len(y_kut))
plt.title("Метод Эйлера")
plt.xlabel('Координата X', size=14)
plt.ylabel('Координата Y', size=14)
plt.plot(x, y, 'ro', x_new, y_new)
plt.grid(True)
plt.show()

plt.title("Метод Рунге-Кутта")
plt.xlabel('Координата X', size=14)
plt.ylabel('Координата Y', size=14)
plt.plot(x, y, 'ro', x_new, y_kut)
plt.grid(True)
plt.show()
