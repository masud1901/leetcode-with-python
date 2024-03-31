n = 5
limit =2

# Output: 3


result = []

for i in range(limit+1):
    for j in range(limit+1):
        for k in range(limit+1):
            if i+j+k == n and [i, j, k] not in result:
                result.append([i,j,k])

print(len(result))