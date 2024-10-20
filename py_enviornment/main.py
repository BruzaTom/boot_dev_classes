def num_possible_orders(num_posts):
    total = 1
    for i in range(1, num_posts + 1):
        total += total * (num_posts - i)
    return total