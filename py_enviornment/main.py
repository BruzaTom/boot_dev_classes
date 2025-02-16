def power_set(input_set):
    if input_set == []:
        return [[]]
    lst = []
    first = input_set[0]
    cut = power_set(input_set[1:])
    for set in cut:
        combo = [first]
        combo.extend(set)
        lst.append(combo)
        lst.append(set)
    return lst
