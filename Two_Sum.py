# nums = [2, 7, 11, 15]
nums = [3, 3]
# target = 9
target = 6


for i in range(len(nums)):
    check = target - nums[i]
    temp = nums[i]
    nums[i] = None
    if check in nums and nums.index(check) != i:
        print([i, nums.index(check)])
