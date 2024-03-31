n = 1024
n = -8
n = -16
# n=-12

# output = True


num = 6
if n<0:
    binary_string = bin(n)
    # binary_string = bin(n)[3:]
else:
    binary_string = bin(n)[2:]

print(binary_string)
count = 0

for i in binary_string:
    # print(i)
    if i == "1":
        count += 1

# print(count)

