from sympy import *

init_printing(use_unicode=False, wrap_line=False)

x = Symbol('x')
# out = integrate(x**2 + x + 1, x)
# print(out)

# out = integrate(x**2 * exp(x) * cos(x), x)
# print(out)

# out = integrate((x - 1)*exp(x)/(x*exp(x) + 1),x)
# print(out)

out = integrate(x *exp(x)/(x*exp(x) + 1),x)
print(out)