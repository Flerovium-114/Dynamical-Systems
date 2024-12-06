import numpy as np
import matplotlib.pyplot as plt

e = 0.1
a1 = (3 - np.sqrt(1 - 8*(e**2)))/(4*(1+(e**2)))  # a-
a2 = (3 + np.sqrt(1 - 8*(e**2)))/(4*(1+(e**2)))  # a+
print('a1 = ', a1)
print('a2 = ', a2)

def E_by_E0(a1,e,a):
    return ((a1**2)*((a1**2)*(1+e**2) - 2*a1 + 1))/(a**2 * (a**2 * (1+e**2) - 2*a + 1))

a = np.linspace(a1 , a2+1 , 100)
E_ratio = E_by_E0(a1, e, a)

plt.plot(a, E_ratio)
plt.grid(True)
plt.xlabel('a')
plt.ylabel('$\\frac{E(t_{max})}{E_{0}}$')
plt.title('$\\frac{E(t_{max})}{E_{0}}$ vs a')
plt.show()   


#print(E_by_E0(a1, e, a2))
E_ratio_max = max(E_ratio)

print('E_ratio_max = ', E_ratio_max)   # print maximum value of E(tmax)/E0
for i in range(len(E_ratio)):
    if E_ratio[i] == E_ratio_max:
        #print('i = ', i)
        break

print('a_for E_ratio_max = ', a[i])  # Finding value of a for which E_ratio is maximized, comes out to be close to a+ (a2)
E_ratio_max_th = ((3*a1 - 1) * (1 - a1))/((3*a2 - 1)*(1 - a2))
print('E_ratio_max_th = ', E_ratio_max_th)
