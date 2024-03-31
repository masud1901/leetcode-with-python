num = 11891
# num = 1100099999
# num = 88888
# Output: 99009
# num = 90
# num = 991
# num = 887

for_bigger = list(str(num)[:])
for_smaller = list(str(num)[:])


most_important_value = for_bigger[0]
if most_important_value == "9":
    for i in range(1, len(for_bigger)):
        if for_bigger[i] != "9":
            most_important_value = for_bigger[i]
            break


# print(type(most_common_value))

bigger_number = 0

for i in range(len(for_bigger)):
    if for_bigger[i] == most_important_value:
        for_bigger[i] = "9"

bigger_number = int("".join(for_bigger))

smaller_number = 999999
if for_smaller[0] == "9":
    most_important_value = "9"
for i in range(len(for_smaller)):
    if for_smaller[i] == most_important_value:
        for_smaller[i] = "0"

smaller_number = int("".join(for_smaller))


print(bigger_number, smaller_number)
