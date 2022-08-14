def sinle_nums(nums):
    unique = []
    res = 0
    for i in nums:
        if i not in unique:
            unique.append(i)
        else:
            unique.remove(i)
    res = unique[0]
    return res
nums = [2,2,1]
print(sinle_nums(nums))
