# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임
def babygin(player):
    for i in range(10):
        if player[i] == 3:
            return True
        if i > 7:continue
        if player[i] and player[i+1] and player[i+2]:
            return True
    return False

for tc in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    for i in range(0, 11, 2):
        player1[cards[i]] += 1
        player2[cards[i+1]] += 1
        if i >= 4:
            score1 = babygin(player1)
            if score1:
                print('#{} 1'.format(tc))
                break
            score2 = babygin(player2)
            if score2:
                print('#{} 2'.format(tc))
                break
    else:
        print('#{} 0'.format(tc))


# # 오답 : 10개의 테스트케이스 중 8개가 맞았습니다
# # player1이 먼저 받고 player2가 다음 턴이라는 것을 생각하지 않고 같은 장수를 받았을 때로 생각
# def babygin(player):
#     for i in range(10):
#         if player[i] == 3:
#             return True
#         if i > 7:continue
#         if player[i] and player[i+1] and player[i+2]:
#             return True
#     return False

# for tc in range(1, int(input())+1):
#     cards = list(map(int, input().split()))
#     player1 = [0] * 10
#     player2 = [0] * 10
#     for i in range(0, 11, 2):
#         player1[cards[i]] += 1
#         player2[cards[i+1]] += 1
#         if i >= 4:
#             score1 = babygin(player1)
#             score2 = babygin(player2)
#             if score1 and score2:
#                 print('#{} 0'.format(tc))
#                 break
#             elif score1:
#                 print('#{} 1'.format(tc))
#                 break
#             elif score2:
#                 print('#{} 2'.format(tc))
#                 break
#     else:
#         print('#{} 0'.format(tc))