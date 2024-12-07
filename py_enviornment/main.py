def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    #print(lst1,'\n',lst2)
    return merge(left, right)


def merge(first, second):
    final = []
    i, j = 0, 0
    #print(first,second)
    while((i < len(first)) & (j < len(second))):
            if first[i] <= second[j]:
                final.append(first[i])
                i += 1
            else:
                final.append(second[j])
                j += 1
    final.extend(first[i:])
    final.extend(second[j:])
    return final


