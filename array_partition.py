def arr(nums):
    nums.sort()
    i = 0
    sum = 0
    while i < len(nums) - 1:
        sum += nums[i]
        i += 2
    return sum
nums = [1,4,3,2]
print(arr(nums))
