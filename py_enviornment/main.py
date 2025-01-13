def quick_sort(nums, low, high):
    if low < high:
        i = partition(nums, low, high)
        quick_sort(nums, 0, i-1) #left
        quick_sort(nums, i+1, high) #right
        #do not assighn a left and right variable
        

def partition(nums, low, high):
    pivit = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivit:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
    temp = nums[i]
    nums[i] = nums[high]
    nums[high] = temp
    return i
