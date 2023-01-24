import matplotlib.pyplot as plt
from math import e

# Example function
def f(x):
     return(((x**2 + x -1)**11)/(1 + e**-x))

# Derivative of the function
def df(x):
     return(((22*x*e**(2*x) + 22*x*e**x + 11*e**(2*x) + 11*e**x) * ((x** 2+x-1)**10) + ((x**2 + x -1)**11) * (e**x)) / ((e**x + 1)**2))

# Initial approach
x0 = -0.5

# Accurate error
precision = 1e-6

k = 1
# Store errors and iterations
errors = []
k_graph = []

# Newton approximation
x0_newton = x0
x0_newton = x0_newton - (f(x0_newton) / df(x0_newton))
print("\n\t\t\t >>> Newton's Method - Table <<<")
print("\n\tIteration \t x0_newton \t\t\t f(x[k]) \t\tApproximate absolute error\n")
while((abs((f(x0_newton) / df(x0_newton))) > precision)):
     x0_newton = x0_newton - (f(x0_newton) / df(x0_newton))
     errors.append((f(x0_newton) / df(x0_newton)))
     k_graph.append(k)
     print('\t ', k, ' \t', x0_newton, ' \t', f(x0_newton), ' ', (f(x0_newton) / df(x0_newton)))
     k = k+1
print("\n\tFinal Root Approximation:",round(x0_newton,6))
    
# Plot absolute error graph by iterations
plt.plot(k_graph , errors)
plt.title("Newton's Method - Approximate Absolute Error Graph")
plt.xlabel("Iterations")
plt.ylabel(["Approximate error"])
plt.show()
