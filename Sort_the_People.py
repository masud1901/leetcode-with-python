names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]


names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]

lst = []

for i in range(0, len(names)):
    lst.append([names[i], heights[i]])


lst.sort(key=lambda x: x[1])

lst2 = []
for i in range(len(lst)):
    lst2.append(lst[i][0])


print(lst2)


lst3 = []
while i >= 0:

    lst3.append(lst2[i])
    i -= 1

print(lst3)
