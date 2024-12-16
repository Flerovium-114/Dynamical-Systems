# Dynamical-Systems 
## Introduction
- Part of my assignment for the course **AS5430 - Stability of Shear Flows** at **IIT MADRAS**. 
This repository contains Python based codes for solving some simple problems on dynamical systems. I have attached the assignment PDF and the codes are numbered according to the question numbers. I suggest to go through the reference attached for the basics in Dynamical systems and a detailed study on Stability of Shear Flows.

## Method for solving a second order ODE using RK-4 integration
We have the equation:

We aim to solve the second-order ODE:

![Equation](https://latex.codecogs.com/png.latex?\frac{d^2\theta}{dt^2}+\mu\frac{d\theta}{dt}+\omega_0^2\sin^2\theta=0)

https://latex.codecogs.com/svg.image?&space;
\[
\frac{d^2\theta}{dt^2} + \mu\frac{d\theta}{dt} + \omega_0^2 \sin^2\theta = 0
\]

To simplify, we rewrite the equation as two first-order ODEs:

- \( X_1 = \theta \)
- \( X_2 = \frac{d\theta}{dt} \)

Thus:
\[
\frac{dX_1}{dt} = X_2
\]
\[
\frac{dX_2}{dt} = -\mu X_2 - \omega_0^2 \sin^2(X_1)
\]


## Reference:
1) **Hydrodynamic Instabilities**, *FRANÇOIS CHARRU*, *University of Toulouse*, *Cambridge University Press*
