#Importing necessary modules
import math
import numpy as np
import matplotlib.pyplot as plt

def f(t, x1, x2, w0, mu):
    dx1_dt = x2 
    dx2_dt = -mu*x2 - w0**2*math.sin(x1)  
    return dx1_dt, dx2_dt  

#RK4 method
def rk_4(f, t, x1, x2, mu, w0, h, T):
    x1_values = [x1]
    x2_values = [x2]
    time_values = [t]

    while t < T:
        k1_x1, k1_x2 = f(t, x1, x2, w0, mu)
        k2_x1, k2_x2 = f(t + 0.5 * h, x1 + 0.5 * h * k1_x1, x2 + 0.5 * h * k1_x2, w0, mu)
        k3_x1, k3_x2 = f(t + 0.5 * h, x1 + 0.5 * h * k2_x1, x2 + 0.5 * h * k2_x2, w0, mu)
        k4_x1, k4_x2 = f(t + h, x1 + h * k3_x1, x2 + h * k3_x2, w0, mu)

        x1 = x1 + (h / 6.0) * (k1_x1 + 2 * k2_x1 + 2 * k3_x1 + k4_x1)
        x2 = x2 + (h / 6.0) * (k1_x2 + 2 * k2_x2 + 2 * k3_x2 + k4_x2)

        t = t + h

        x1_values.append(x1)
        x2_values.append(x2)
        time_values.append(t)

    return time_values, x1_values, x2_values

t = 0.0       
mu = 0
w0 = math.sqrt(9.81)      
h = 0.001        
T = 10
tolerance = 0.001
x1_0 = 0
x2_0 = np.linspace(2, 6.26418, 25)

plt.figure(figsize=(4, 3))
labels = []
for k in range(len(x2_0)):
    time_values, x1_values, x2_values = rk_4(f, t, x1_0, x2_0[k], mu, w0, h, T)
    for i in range(len(x2_values)):
        if x2_values[i] < tolerance:
            break
    time_values = time_values[: i+1]
    x1_values = x1_values[: i+1]
    x2_values = x2_values[: i+1]
    plt.plot(x1_values, time_values)
    plt.grid()
    plt.xlabel('$\\theta$')
    plt.ylabel(t)
    plt.title('time taken to reach($\\pi,0)$')
    print('time_values[i] = ', time_values[i])
plt.show()
