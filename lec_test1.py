import sympy as sym

x, y, z = sym.symbols('x y z')
expr = sym.sin(x) + sym.log(x, 10) - x
solve_expr = sym.solveset(expr)
print(solve_expr)


expr = 2**x - sym.log(x, 10) - sym.cos(x)**-1
solve_expr = sym.solveset(expr)
print(solve_expr)
