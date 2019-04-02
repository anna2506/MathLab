import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from math import exp

def mnkGP(x,y): # функция которую можно использзовать в програме
              n=len(x) # количество элементов в списках
              x_linespace = np.linspace(np.min(x), np.max(x), 100)
              s11 = float(sum([2*(x[i]**2) for i in range(0, n)]))  # сумма 2*x^2
              s12 = float(sum([2*exp(-x[i])*x[i] for i in range(0, n)]))  # 2*exp(-x)*x
              s13 = float(sum([2*x[i] for i in range(0, n)]))  # сумма 2*x
              s21 = s12
              s22 = float(sum([2*exp(-2*x[i]) for i in range(0, n)]))  # сумма 2*exp(-2x)
              s23 = float(sum([2*exp(-x[i]) for i in range(0, n)]))  # сумма 2*exp(-x)
              s31 = float(sum([2*x[i] for i in range(0, n)]))  # сумма 2*x
              s32 = s23
              s33 = 2.0
              coef1 = float(sum([2*y[i]*x[i] for i in range(0, n)]))  # сумма 2*y*x
              coef2 = float(sum([2*exp(-x[i])*y[i] for i in range(0, n)]))  # сумма 2*exp(-x)*y
              coef3 = float(sum([2*y[i] for i in range(0, n)]))  # сумма 2*y
              A = np.array([[s11, s12, s13], [s21, s22, s23], [s31, s32, s33]])
              B = np.array([coef1, coef2, coef3])
              C = np.linalg.solve(A, B)
              a = C[0]
              b = C[1]
              c = C[2]
              s4 = [a*X+b*exp(-X)+c for X in x_linespace] # список значений гиперболической функции
              plt.xlabel('Координата X', size=14)
              plt.ylabel('Координата Y', size=14)
              plt.plot(x, y, color='r', linestyle=' ', marker='o', label='Data(x,y)')
              plt.plot(x_linespace, s4, color='b', linewidth=2, label='Data(x,f(x)=a*x+b*exp(-x)+c')
              plt.legend(loc='best')
              plt.grid(True)
              plt.show()
x = np.array([0.231, 0.564, 0.896, 1.229, 1.561, 1.894, 2.227, 2.559, 2.892])

y = np.array([-2.748, -2.932, -3.070, -3.391, -3.648, -3.737, -3.911, -4.294, -4.506]) # данные для проверки по функции y=a/x+b*exp(x)+c

mnkGP(x, y)