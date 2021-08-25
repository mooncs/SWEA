# 3499. 퍼펙트 셔플
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) >0:
        if len(left) > 0 and len(right) > 0:
                result.append(left.pop(0))
                result.append(right.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
    return result

# 분할 함수
def division(arr):
    if len(arr) == 1:
        return arr
    if N%2:
        middle = N//2 + 1
    else:
        middle = N//2
    left, right = cards[:middle], cards[middle:]

    return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input().split()
    shuffled = division(cards)
    print('#{} {}'.format(tc, ' '.join(shuffled)))
###############################################################################
# def shuffle():
#     if N%2:
#         middle = N//2 + 1
#     else:
#         middle = N//2
#     deck1 = cards[:middle]
#     deck2 = cards[middle:]
#     pdeck = []
#     for i in range(len(deck2)):
#         pdeck.append(deck1[i])
#         pdeck.append(deck2[i])
#     if N%2:
#         pdeck.append(deck1.pop())

#     return pdeck

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cards = input().split()
#     shuffled = shuffle()
#     print('#{} {}'.format(tc, ' '.join(shuffled)))
