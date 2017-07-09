__author__ = 'Ahadu Tsegaye Abebe - 09/07/17'

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,20)
cosx = [np.cos(n) for n in x]
sinx = [np.sin(n) for n in x]

plt.plot(x,cosx)
plt.plot(x,sinx)

plt.show()