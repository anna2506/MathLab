from math import sin, cos
def func(x):
    return x*sin(3*x)

a, b, x1, x2 = 0, 1, 0, 0
step1 = float(b - a)/200
step2 = float(b - a)/400
trapezium = 0
simpson = 0

#Метод трапеций
for i in range(200):
    if i == 0 or i == 199:
        trapezium += step1*func(x1)/2
    else:
        trapezium += step1*func(x1)
    x1 += step1
print(trapezium)

#Метод Симпсона
for i in range(400):
    if i == 0 or i == 399:
        simpson += step2/3*func(x2)
    else:
        if i % 2 == 0:
            simpson += 2*step2/3*func(x2)
        else:
            simpson += 4*step2/3*func(x2)
    x2 += step2
print(simpson)

print(-1/3*cos(3) + 1/9*sin(3))
