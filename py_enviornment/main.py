def fib(n):
    if n <= 1:
        return n
    current = 0
    parent = 1
    gp = 0
    for i in range(0, n-1):
        current = parent + gp
        gp = parent
        parent = current
    return current
