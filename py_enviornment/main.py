def selection_sort(nums):
    for t in range(0, len(nums)):
        small = t
        for i in range(small+1, len(nums)):
            if nums[i] < nums[small]:
            
                small = i
        nums[t], nums[small] = nums[small], nums[t]
    return nums

