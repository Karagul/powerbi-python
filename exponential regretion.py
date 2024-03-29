import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit 
import numpy as np

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# xdata = np.linspace(0, 4, 50)
# y = func(xdata, 2.5, 1.3, 0.5)
# np.random.seed(1729)
# y_noise = 0.2 * np.random.normal(dataset.x)
# ydata = y + y_noise
plt.plot(dataset.x, dataset.y, 'o')

popt, pcov = curve_fit(func, dataset.x, dataset.y)
popt

plt.plot(dataset.x, func(dataset.x, *popt), 'r-',label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()