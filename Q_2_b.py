import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def equilibrium(x, mu, delta):
    return mu*x - delta * x**3

def jacobian(x, mu, delta):
    return mu - 3 * delta * (x**2)

delta = 1
mu_values = np.linspace(-1, 1, 75)
x_stable = []
x_unstable = []

stable_mu = []
unstable_mu = []

plt.figure(figsize=(8, 6))

for mu in mu_values:
    initial_guess = [0, 1.0, -1.0]
    roots = set()

    for guess in initial_guess:
        root = fsolve(equilibrium, guess, args = (mu, delta))[0]

        if root not in roots:
            roots.add(root)
            stability = jacobian(root, mu, delta)

            if stability <= 0:
                x_stable.append(root)
                stable_mu.append(mu)
            else:
                x_unstable.append(root)
                unstable_mu.append(mu)
 
plt.plot(stable_mu, x_stable, 'o', label='Stable Equilibrium', markersize = 4)
plt.plot(unstable_mu, x_unstable, 'o', label='Unstable Equilibrium', markersize = 4)
plt.axvline(x=0, color='k', linestyle='--', label='Bifurcation Point')
plt.xlabel('$\\mu$')
plt.ylabel('$x$')
plt.title('Bifurcation Diagram for $\\frac{dx}{dt} = \\mu x - \\delta x^3$')
plt.legend()
plt.grid(True)
plt.show()
