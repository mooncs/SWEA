# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임

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
    