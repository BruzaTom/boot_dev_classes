def decayed_followers(intl_followers, fraction_lost_daily, days):
    ret = 1.00 - fraction_lost_daily
    if fraction_lost_daily == 0:
        return intl_followers
    return intl_followers * (ret ** days)
