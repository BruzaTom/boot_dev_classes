def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        med = (low + high) // 2
        if arr[med] == target:
            return True
        elif arr[med] < target:
            low = med + 1
        else:
            high = med - 1
    return False
