import matplotlib.pyplot as plt

#метод Лагранжа
x = [0.172, 0.567, 1.113, 2.119, 2.769]
y = [-7.057, -5.703, -0.132, 1.423, 2.832]

def lagranz(x, y, t):
    z = 0
    for i in range(len(y)):
        up, down = 1, 1
        for j in range(len(x)):
            if i is j:
                continue
            else:
                up *= (t - x[j])
                down *= (x[i] - x[j])
        z += y[i] * up / down
    return z


xnew = []
add = min(x)
step = (max(x) - min(x)) / float(100)
for i in range(100):
    xnew.append(add)
    add += step
    if i == 99:
        xnew.append(max(x))
        break
ynew = [lagranz(x, y, i) for i in xnew]
plt.plot(x, y, 'ro', xnew, ynew)
plt.grid(True)
plt.show()

#Метод интерполяционного сплайна
coef = [0.172, 0.576, 0.576, 1.113, 1.113, 2.119, 2.119, 2.769]

C = [ -7.057, -5.703, -5.703, -0.132, -0.132, 1.423, 1.423, 2.832]
A = [0.0]*4
B = [0.0]*4
for i in range(0, 8, 2):
    A[i//2] = (C[i+1] - C[i])/(coef[i+1] - coef[i])
    B[i//2] = C[i] - (coef[i]*A[i%4])
for i in range(4):
    print("A[" + str(i + 1) + "] coef is " + str(A[i]) + "\n")
    print("B[" + str(i + 1) + "] coef is " + str(B[i]) + "\n")

plt.plot(x, y, x, y, 'ro')
plt.grid(True)
plt.show()

