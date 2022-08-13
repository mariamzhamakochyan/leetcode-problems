def arr(nums):
    odd_nums = []
    even_nums = []
    for i in nums:
        if i  % 2 == 0:
           even_nums.append(i)
        else:
           odd_nums.append(i)
        res = odd_nums + even_nums
    return res
nums = [1, 7, 9, 4, 6, 2, 11, 72, 99]
print(arr(nums))
