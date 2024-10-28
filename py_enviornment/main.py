import math

def log_scale(data, base):
    lst = []
    for num in data:
        lst.append(math.log(num, base))
    return lst
