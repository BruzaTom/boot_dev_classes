def does_name_exist(first_names, last_names, full_name):
    split = full_name.split()
    for first in first_names:
        for last in last_names:
            if first == split[0] and last == split[1]:
                return True
    return False


