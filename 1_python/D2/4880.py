# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임
# 체크체크 -> 비겼을 때를 체크해주지 않아서 문제가 되었다.
# 비긴 것을 포함하도록 elif를 else로 변경
def RSP(arr):
    if len(arr) == 1:
        return arr[0][0], arr[0][1]
    
    middle = (len(arr)+1)//2
    
    idx1, card1 = RSP(arr[:middle])
    idx2, card2 = RSP(arr[middle:])
    
    # 1가위, 2바위, 3보
    if card2-card1==1 or card2-card1==-2:
        return idx2, card2
    else:
        return idx1, card1


T = int(input())
for tc in range(1, T+1):
    # 인원수 N
    N = int(input())
    cards = list(map(int, input().split()))
    for idx, card in enumerate(cards):
        cards[idx] = [idx, card]
    
    idx, card = RSP(cards)
    print('#{} {}'.format(tc, idx+1))

##############################################################
# # 실패!!!!!!!!!!!!!!!!
# def RSP(arr):
#     if len(arr) == 1:
#         return arr[0][0], arr[0][1]
    
#     else:
#         if len(arr)%2:
#             middle = len(arr)//2 + 1
#             idx1, card1 = RSP(arr[:middle])
#             idx2, card2 = RSP(arr[middle:])
#         else:
#             middle = len(arr)//2
#             idx1, card1 = RSP(arr[:middle])
#             idx2, card2 = RSP(arr[middle:])

#         # 1가위, 2바위, 3보
#         if card2-card1==1 or card2-card1==-2:
#             return idx2, card2
#         elif card1-card2==1 or card1-card2==-2:
#             return idx1, card1


# T = int(input())
# for tc in range(1, T+1):
#     # 인원수 N
#     N = int(input())
#     cards = list(map(int, input().split()))
#     for idx, card in enumerate(cards):
#         cards[idx] = [idx, card]
    
#     idx, card = RSP(cards)
#     print('#{} {}'.format(tc, idx+1))


##############################################################
# kkyul    
def win(num_a, rcp_a, num_b, rcp_b):
    if rcp_b - rcp_a == 1 or rcp_b - rcp_a == -2:
        return num_b, rcp_b
    else:
        return num_a, rcp_a

def divided(st, ed):
    if st==ed:
        return st, people[st]
    mid = (st+ed) // 2

    return win(*divided(st,mid), *divided(mid+1, ed))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    people = list(map(int, input().split()))

    ans = divided(0, N-1)

    print('#{} {}'.format(tc, ans[0]+1))