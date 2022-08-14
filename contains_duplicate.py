def duplicates(nums):
    a =[]
    for i in range(len(nums)):
        if nums[i] not in a:
            a.append(nums[i])
        else:
            return True
    return False
nums = [1,2,3,1]
print(duplicates(nums))
