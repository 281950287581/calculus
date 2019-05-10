import sympy


x = sympy.Symbol('x')
# f = sympy.E ** x + 2 * x
# print(sympy.integrate(f,x))
# f = (x*sympy.E**x - sympy.E**x)/(1+x*sympy.E**x)
f = (x - 1)*sympy.E**x/(x*sympy.E**x+1)
out = sympy.integrate(f, x)
print(out)