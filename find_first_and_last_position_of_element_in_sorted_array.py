nums = [5, 7, 7, 8, 8, 10]
target = 11
# Output: [3,4]


def binary_search(nums: list, target: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            return True
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False


def floor_search(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = int(left + (right - left) / 2)
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return right


def ceil_search(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = int(left + (right - left) / 2)
        if target <= nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return left

if binary_search(nums, target):
    ceilIndex = ceil_search(nums, target)
    floorIndex = floor_search(nums, target)
    print([ceilIndex, floorIndex])
else:
    print([-1, -1])
