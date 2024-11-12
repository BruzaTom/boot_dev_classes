def find_last_name(names_dict, first_name):
    if first_name in names_dict:
        return names_dict[first_name]

def find_last_name2(names_dict, first_name):
    try:
        return names_dict[first_name]
    except KeyError:
        return None
