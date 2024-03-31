text = "loonbalxballpoon"
# Output: 2


from collections import Counter


charCounter = dict(Counter(text.lower()))
lst = []

dct = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

for i in charCounter.keys():
    if i in dct:
        dct[i] = charCounter[i]

lst.append(dct["b"])
lst.append(dct["a"])
lst.append(int(dct["l"] / 2))
lst.append(int(dct["o"] / 2))
lst.append(dct["n"])

print(charCounter)

print(min(lst))
