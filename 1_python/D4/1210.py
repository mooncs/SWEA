# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
# for _ in range(10):
#     T = int(input())
#     ladder = [list(map(int, input().split())) for _ in range(100)]

#     r = 99
#     c = 0
#     for i in range(100):
#         if ladder[r][i] == 2:
#             c = i
#             break
    
#     while r:
#         if 0<c<99:
#             if not ladder[r][c-1] and not ladder[r][c+1] and ladder[r-1][c]:
#                 r -= 1
#             elif ladder[r][c-1]:
#                 while 0<c and ladder[r][c-1]:
#                     c -= 1
#                 r -= 1
#             elif ladder[r][c+1]:
#                 while c<99 and ladder[r][c+1]:
#                     c += 1
#                 r -= 1
#         elif c == 0:
#             if not ladder[r][c+1] and ladder[r-1][c]:
#                 r -= 1
#             elif ladder[r][c+1]:
#                 while c<99 and ladder[r][c+1]:
#                     c += 1
#                 r -= 1
#         else:
#             if not ladder[r][c-1] and ladder[r-1][c]:
#                 r -= 1
#             elif ladder[r][c-1]:
#                 while 0<c and ladder[r][c-1]:
#                     c -= 1
#                 r -= 1
    
#     print("#{} {}".format(T, c))


# 2
for _ in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    r = 99  # 2인 지점을 찾기 위해 열을 99로 지정
    c = 0
    dr = [-1, 0, 0]     # 상, 좌, 우
    dc = [0, -1, 1]
    d = 0   # 현 이동 방향을 지시
    # 2인 열을 찾고 현재의 열로 지정
    for i in range(100):
        if ladder[r][i] == 2:
            c = i
            break
    # 열이 0이 될 때까지
    while r:
        # 좌우로 와리가리하는 것을 방지하기 위해, 오른쪽으로 가는 중이 아니었고, 열이 0보다 크고 사다리가 갈 수 있는 곳(1로 채워진 곳)인지 확인
        if d!=2 and c>0 and ladder[r][c-1]:
            # 왼쪽으로 갈 수 있는 구간이면 왼쪽으로 방향 지정
            d = 1
        # 왼쪽으로 가는 것과 동일하게, 오른쪽으로 갈 수 있는 조건인지 확인
        elif d!=1 and c<99 and ladder[r][c+1]:
            # 오른쪽으로 갈 수 있는 구간이면 오른쪽으로 방향 지정
            d = 2
        # 좌우 다 갈 수 없다면 위로 갈 수 있으니 위로 이동
        else:
            d = 0
        # 방향에 맞게 현 위치를 갱신
        r += dr[d]
        c += dc[d]
    
    print("#{} {}".format(T, c))
