# 1220. [S/W 문제해결 기본] 5일차 - Magnetic
for tc in range(1, 11):
    # 정사각형 테이블의 한 변의 길이
    n = int(input())
    sq = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for c in range(n):
        stack = []
        for r in range(n):
            if sq[r][c] == 1:
                stack.append(1)
            
            elif sq[r][c] == 2 and stack:
                stack.clear()
                cnt += 1

    print('#{} {}'.format(tc, cnt))


#########################################################################
# # fail
# # cnt 위치 변경 -> pass
# for tc in range(1, 11):
#     # 정사각형 테이블의 한 변의 길이
#     n = int(input())
#     sq = [list(map(int, input().split())) for _ in range(n)]
#     cnt = 0
#     for c in range(n):
#         flag = 0
#         for r in range(n):
#             if sq[r][c] == 1 and flag == 0:
#                 flag = 1
#             elif sq[r][c] == 2 and flag == 1:
#                 cnt += 1
#                 flag = 0

#     print('#{} {}'.format(tc, cnt))


#########################################################################
# # fail
# # a = q.pop()으로 잘못적은거 변경... -> pass
# for tc in range(1, 11):
#     # 정사각형 테이블의 한 변의 길이
#     n = int(input())
#     sq = [list(map(int, input().split())) for _ in range(n)]
#     cnt = 0
#     for c in range(n):
#         q = []
#         for r in range(n):
#             if sq[r][c] != 0:
#                 q.append(sq[r][c])
        
#         while len(q)>1:
#             a = q.pop(0)
#             if a == 1 and q[0]==2:
#                 q.pop(0)
#                 cnt += 1

#     print('#{} {}'.format(tc, cnt))
