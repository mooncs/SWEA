# 1865. 동철이의 일 분배
def dfs(idx, perc):
    global max_perc
    if max_perc >= perc:return
    if idx == n:
        max_perc = max(perc, max_perc)
        return
    for i in range(n):
        if check[i]:continue
        check[i] = 1
        dfs(idx+1, perc*(arr[idx][i]/100))
        check[i] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    check = [0]*n
    max_perc = 0
    dfs(0, 1)
    print('#{} {:.6f}'.format(tc, max_perc*100))


# # 시간 초과
# def dfs(idx, perc):
#     global max_perc
#     if idx == n:
#         max_perc = max(perc/10000, max_perc)
#     for i in range(n):
#         if check[i]:continue
#         check[i] = 1
#         dfs(idx+1, perc*arr[idx][i])
#         check[i] = 0

# for tc in range(1, int(input())+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     check = [0]*n
#     max_perc = 0
#     dfs(0, 1)
#     print('#{} {:.6f}'.format(tc, max_perc))