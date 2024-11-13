def remove_duplicates(nums):
    list = []
    for num in nums:
        if num not in list:
            list.append(num)
    return list