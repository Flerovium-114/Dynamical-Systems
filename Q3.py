import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

alpha_values = [0, 0.01, -0.01]  # α = 0 and a small non-zero value
w_2_vals = np.linspace(0, 2, 75) 
plt.figure(figsize=(8, 6))

def equilibrium(theta, w_2, alpha):
    return w_2 * (theta - alpha) - np.sin(theta)

def second_derivative(theta, w_2):
    return w_2 - np.cos(theta)

stable_theta = []
unstable_theta = []
stable_w_2 = []
unstable_w_2 = []
for alpha in alpha_values:
    all_theta_roots = []  
    stability_flags = []  

    for w_2 in w_2_vals:
        initial_guesses = [0.0, 1.0, -1.0]  
        roots = set()  
        stability = []  
        
        for guess in initial_guesses:
            root = fsolve(equilibrium, guess, args=(w_2, alpha))[0]
            #root = round(root, 8)  # Round to avoid precision issues
        
            if root not in roots: 
                roots.add(root)
                # Determine stability
                stability_value = second_derivative(root, w_2)
                stability.append(stability_value > 0) 

        all_theta_roots.append(list(roots))
        stability_flags.append(stability)

    # Flatten results for plotting
    flattened_roots = [root for sublist in all_theta_roots for root in sublist]
    flattened_w_2 = [w_2 for w_2, roots in zip(w_2_vals, all_theta_roots) for _ in roots]
    flattened_stability = [stab for sublist in stability_flags for stab in sublist]

    # Plot stable and unstable equilibrium points
    stable_points = [root for root, stable in zip(flattened_roots, flattened_stability) if stable]
    unstable_points = [root for root, stable in zip(flattened_roots, flattened_stability) if not stable]
    stable_w_2 = [w for w, stable in zip(flattened_w_2, flattened_stability) if stable]
    unstable_w_2 = [w for w, stable in zip(flattened_w_2, flattened_stability) if not stable]
    stable_w = np.sqrt(stable_w_2)
    unstable_w = np.sqrt(unstable_w_2)

    plt.plot(stable_w, stable_points, 'o', label='Stable Equilibrium', markersize = 4)
    plt.plot(unstable_w, unstable_points, 'o', label='Unstable Equilibrium', markersize = 4)
    plt.xlabel('$\\mu$')
    plt.ylabel('$x$')
    plt.title('Bifurcation Diagram')
    plt.legend()
    plt.grid(True)
    plt.show()
