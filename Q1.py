# Importing necessary modules
import math
import numpy as np
import matplotlib.pyplot as plt

# Defining the DOFs
def f(t, x1, x2, w0, mu):
    dx1_dt = x2 
    dx2_dt = -mu*x2 - w0**2*math.sin(x1)  
    return dx1_dt, dx2_dt  

# RK4 method
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
x2_0 = 0.5
mu_0 = 0
mu_pi = -1
w0 = math.sqrt(9.81)      
h = 0.01        
T = 10
x1_pi = np.linspace(2, 4, 10) 
x1_0 = np.linspace(-1, 1, 10)
y_values = np.linspace(-10, 10, 15)
pi_values = [math.pi]*15 

'''# Rough calculation needed for Question 5
x1_0 = 0
x2_0 = 6.2642
time, x1, x2 = rk_4(f,t, x1_0, x2_0, mu_0, w0, h, T )
plt.plot(x1, x2)
plt.show()'''

#  iterate through x1 values
for i in range(len(x1_0)):
    time_values, x1_values, x2_values = rk_4(f, t, x1_0[i], x2_0, mu_0, w0, h, T)
    #time_values, x1_values, x2_values = rk_4(f, t, x1_pi[i], x2_0, mu_pi, w0, h, T)
    plt.plot(x1_values, x2_values, 'b')
    
    # Keep changing according to where we need arrows to show direction of movement
    desired_x1_positions = [-0.5, -0.1, -0.05, 0.05, 0.1, 0.5]
    #desired_x1_positions = [2, 2.5, 3, 3.5, 4, 4.5]
    
    # Find the closest indices in x1_values for the desired x1 positions
    for x1_target in desired_x1_positions:
        idx = np.argmin(np.abs(np.array(x1_values) - x1_target))
        
        # Plot an arrow at the selected index
        if idx > 0:  # Make sure idx is valid
            plt.annotate('', xy=(x1_values[idx], x2_values[idx]), 
                         xytext=(x1_values[idx-1], x2_values[idx-1]),
                         arrowprops=dict(facecolor='red', shrink=0.05, width=0.2, headwidth=5, headlength=7))
    plt.xlabel('$\\theta$')
    plt.ylabel('$\dot{\\theta}$')
    plt.title('$\dot{\\theta}$ vs $\\theta$')
    plt.grid(True)
    
#plt.plot(pi_values, y_values, 'g--')
plt.show()
