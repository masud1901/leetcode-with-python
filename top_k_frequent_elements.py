nums = [1, 1, 1, 2, 2, 3]
k = 2

# nums = [3, 0, 1, 0]
# Output: [1,2]



from collections import Counter


count = Counter(nums)
answer = []
for element, count in count.most_common():
    # answer.append(element)
    print(element,count)

# print(answer[:k])