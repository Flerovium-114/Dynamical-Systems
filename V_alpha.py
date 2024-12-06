import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def PE(w, x, a):
    return w**2/2 * (x - a)**2 + np.cos(x) - 1

w_vals = np.linspace(0, 1.4, 5)
#a = np.linspace(-0.5, 0.5, 5)
a = 0.5
#w_vals = [0.8]
x = np.linspace(-2*np.pi, 2*np.pi, 50)
for i in range(len(w_vals)):
    V = PE(w_vals[i], x, a)
    #print(V)
    plt.plot(x, V)
    plt.grid(True)
    plt.title('V vs $\\theta$')
    plt.xlabel('$\\theta$')
    plt.ylabel('V')
plt.show()