def exponential_growth(n, factor, days):
    lst = []
    lst.append(n)
    for i in range(days):
        n = n * factor
        lst.append(n)
    return lst