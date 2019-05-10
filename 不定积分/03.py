import sympy

x = sympy.Symbol('x')
f = (x*sympy.E**x - sympy.E**x)/(1+x*sympy.E**x)
out = sympy.integrate(f, x)
print(out)