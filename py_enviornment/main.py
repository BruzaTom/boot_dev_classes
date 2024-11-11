def get_avg_brand_followers(all_handles, brand_name):
    sum = 0
    for list in all_handles:    
        count = 0
        for tag in list:
            if brand_name in tag:
                count += 1 
        sum += count
    return sum / len(all_handles)
    

