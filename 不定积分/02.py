import sympy

x = sympy.Symbol('x')
out = sympy.integrate(1/x, x)
print(out)