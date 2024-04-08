# nums = [3, 0, 1]
# nums = [2, 0, 1]
nums = [3,1,2]
# nums = [6,4,3,2,0,5]
# nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# output = 2


i = 0
while i < len(nums):


    current = nums[i]

    if current == len(nums):
        i += 1
        continue

    if nums[i] != nums[current]:
        nums[i], nums[current] = nums[current], nums[i]
    else:
        i += 1


for i in range(len(nums)):
    if nums[i] != i:
        print(i)

print(len(nums))
