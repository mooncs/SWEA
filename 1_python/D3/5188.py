# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합
# 1
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        arr[0][i] += arr[0][i-1]
        arr[i][0] += arr[i-1][0]
    for r in range(1, n):
        for c in range(1, n):
            arr[r][c] += min(arr[r-1][c], arr[r][c-1])
    print('#{} {}'.format(tc, arr[n-1][n-1]))

# # 2
# def minsum(r, c):
#     drc = [[0,1], [1,0]]
#     global answer, result
#     if answer < result:
#         return
#     if r == n-1 and c == n-1:
#         answer = result
#         return
#     for i in range(2):
#         dr = r + drc[i][0]
#         dc = c + drc[i][1]
#         if dr < 0 or dr >= n or dc <0 or dc >= n or visited[dr][dc]:
#             continue
#         visited[dr][dc] = 1
#         result += arr[dr][dc]
#         minsum(dr, dc)
#         visited[dr][dc] = 0
#         result -= arr[dr][dc]

        
# for tc in range(1, int(input())+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     visited = [[0]*n for _ in range(n)]
#     answer = 99999
#     result = arr[0][0]
#     visited[0][0] = 1
#     minsum(0, 0)
#     print('#{} {}'.format(tc, answer))