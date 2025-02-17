def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1
    while int(time_left) > 0:
        time_in_country *= factor
        time_left -= time_in_country
        count += 1
    return count


# ?
