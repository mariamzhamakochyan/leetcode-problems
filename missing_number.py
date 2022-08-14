def missin_num(nums):
    nums.sort()
    if nums[0] != 0:
        return 0
    if nums[-1] != len(nums):
        return len(nums)
    for i in range(1, len(nums)):
        res = nums[i - 1] + 1
        if nums[i] != res:
           return res
nums = [3,0,1]
print(missin_num(nums))
