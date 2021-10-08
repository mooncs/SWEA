# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
def dfs(idx, cost):
    global min_cost
    # 현재까지의 비용이 최소 비용보다 크거나 같다면 중단
    if cost >= min_cost:return
    # n개의 제품을 모두 생산했으면 최소 비용 갱신
    if idx == n:
        min_cost = cost
    # n곳의 공장만큼 반복
    for i in range(n):
        # 이번 공장에서 생산하지 않았다면
        if not check[i]:
            # 생산하고
            check[i] = 1
            # 다음 제품과 현재 비용을 값으로 넣고 recursion
            dfs(idx+1, cost+costs[idx][i])
            # 초기화
            check[i] = 0
    
for tc in range(1, int(input())+1):
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    check = [0]*n
    min_cost = 1485
    dfs(0, 0)
    print('#{} {}'.format(tc, min_cost))
