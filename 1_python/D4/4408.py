# 4408. 자기 방으로 돌아가기
# # 예시o, test 2/10
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     move = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 1
#     i, j = 0, 1
#     while i < N-1 and j < N:
#         if move[i][1] < move[j][0] and move[j-1][1] < move[j][0]:
#             j += 1
        
#         else:
#             cnt += 1
#             i += 1

#     print('#{} {}'.format(tc, cnt))