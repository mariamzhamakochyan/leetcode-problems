def sum_of_unique(nums):
    sum = 0
    for i in range(0, len(nums)):
        d = 0
        for j in range(0, i):
            if nums[i] == nums[j]:
               d = 1
               break
        if d == 0:
           print(nums[i])
nums = [1, 2, 3, 4, 5, 5, 5, 5]
print(sum_of_unique(nums))
    
