# Prolog - Auto Generated #
import os, matplotlib.pyplot, uuid, pandas
os.chdir(u'C:/Users/crist/PythonEditorWrapper_f68550d1-ad38-48d7-8fdf-65fb8b86efc5')
dataset = pandas.read_csv('input_df_711e2d0b-0a32-47df-9fff-ca072934534b.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667))
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(x, y)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit 
import numpy as np

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')

popt, pcov = curve_fit(func, xdata, ydata)
popt

plt.plot(xdata, func(xdata, *popt), 'r-',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
popt

plt.plot(xdata, func(xdata, *popt), 'g--',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
                  
# plt.plot(dataset.x,dataset.y,'o', color='red')
# plt.plot(dataset.x,dataset.y, color='blue')
# plt.show()


# Epilog - Auto Generated #
os.chdir(u'C:/Users/crist/PythonEditorWrapper_f68550d1-ad38-48d7-8fdf-65fb8b86efc5')
