def get_estimated_spread(audiences_followers):
    if audiences_followers == []:
        return 0
    num_followers = 0
    for num in audiences_followers:
        num_followers += num
    average = num_followers / len(audiences_followers)
    return average * (len(audiences_followers) ** 1.2)

print(10**3)
