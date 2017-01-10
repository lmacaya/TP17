def mi_factorial(n):
    expr = 1
    if n == 0:
        return 1
    else:
        while n > 0:
            expr *= n
            n -= 1
        return expr