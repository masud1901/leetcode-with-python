ranks = [13, 2, 3, 1, 9]
ranks = [3, 3, 3, 3, 9]
suits = ["a", "a", "a", "a", "a"]
# Output: "Flush"


isFlash = False
isThreeOfAKind = False
isPair = False
isHighCards = False


from collections import Counter

ranksCounter = Counter(ranks)
suitsCounter = Counter(suits)
print(ranksCounter, suitsCounter)


if len(list(dict(suitsCounter).keys())) == 1:
    isFlash = True


most_common_rank = ranksCounter.most_common(1)[0][1]
print(most_common_rank)

if most_common_rank == 3 or most_common_rank == 4:
    isThreeOfAKind = True

if most_common_rank == 2:
    isPair = True

if most_common_rank == 1:
    isHighCards = True

if isFlash:
    print("Flash")
if isThreeOfAKind:
    print("Three of a kind")
if isPair:
    print("Pair")
if isHighCards:
    print("High cards")