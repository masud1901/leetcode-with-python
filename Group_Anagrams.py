strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
strs = ["ddddddddddg", "dgggggggggg"]

answer = {}

for i in range(len(strs)):
    char_list = sorted(strs[i])

    char_list = tuple(char_list)

    if char_list not in answer:
        answer[char_list] = [strs[i]]
    else:
        answer[char_list].append(strs[i])


answer_list = list(answer.values())
print(answer_list)
