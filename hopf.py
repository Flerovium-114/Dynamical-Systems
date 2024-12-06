import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp

def hopf_bifurcation(t, z, mu, delta, w):
    r, phi = z
    drdt = mu * r - delta * r**3
    dphidt = w
    return [drdt, dphidt]

# Parameters
delta = -1  
w = 1  # some constant
mu_values = np.linspace(-1, 1, 10)  
t_span = [0, 50] 
initial_conditions = [0.1, 0.0]  # Initial conditions (r0, phi0)

# 3D plot setup
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

r_steady = []

# Simulate and plot for different mu values
for mu in mu_values:
    # Solve the ODE system
    sol = solve_ivp(hopf_bifurcation, t_span, initial_conditions, args=(mu, delta, w), max_step=0.1)
    r = sol.y[0]
    phi = sol.y[1]

    r_steady.append(r[-1])

    # Convert polar to Cartesian coordinates
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    # Plot in 3D
    ax.plot(x, y, mu, label=f'$\mu$={mu:.2f}')
 
# Set plot labels
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('$\\mu$', fontsize=14)
#ax.set_zlabel(r'$\mu$', fontsize=14)
ax.set_title('3D Plot of Hopf Bifurcation', fontsize=16)
ax.grid(True)
plt.show()
#plt.plot(mu_values, r_final, 'bo')
plt.grid
plt.show()