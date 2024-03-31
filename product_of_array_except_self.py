nums = [1, 2, 3, 4]
# Output: [24,12,8,6]
nums = [5, 9, 2, -9, -9, -7, -8, 7, -9, 10]


def multiply_dict_values(d: dict) -> int:
    result = 1
    for key, value in d.items():
        if value != 0:
            result *= key**value
    return result


import collections

counter = dict(collections.Counter(nums))
counter_only_keys = counter.keys()
# print(counter)
answer = []

for i in range(len(nums)):
    counter[nums[i]] = counter[nums[i]] - 1
    multiplication = multiply_dict_values(counter)
    counter[nums[i]] = counter[nums[i]] + 1
    answer.append(multiplication)


print(answer)
