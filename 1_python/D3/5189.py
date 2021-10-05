# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트
# # 2, 조합 실패
# def permutation(idx):      
#     if idx == n-1:                # idx : 뽑고 있는 자리
#         routes.append(sel)
#     else:
#         for i in range(n-1):      # i: 보고 있는 자리
#             if not check[i]:
#                 sel[idx] = arr[i]
#                 check[i] = 1    # 사용표시
#                 permutation(idx+1)
#                 check[i] = 0    # 원상복귀

# for tc in range(1, int(input())+1):
#     n = int(input())
#     consume = [list(map(int, input().split())) for _ in range(n)]
#     # 순열
#     arr = [i for i in range(1, n)]
#     sel = [0] * (n-1)   # 내가 직접 뽑은거 넣을 리스트
#     check = [0] * (n-1) # 내가 사용한거 체크할 리스트
#     routes = []
#     permutation(0)
#     battery = 10000
#     for route in routes:
#         result, x = 0, 0
#         for r in route:
#             result += consume[x][r]
#             x = r
#         result += consume[x][0]
#         if result < battery:
#             battery = result
#     print('#{} {}'.format(tc, battery))    

# 1
from itertools import permutations

for tc in range(1, int(input())+1):
    n = int(input())
    consume = [list(map(int, input().split())) for _ in range(n)]
    routes = list(permutations([i for i in range(1, n)]))
    battery = 10000
    for route in routes:
        result, x = 0, 0
        for r in route:
            result += consume[x][r]
            x = r
        result += consume[x][0]
        if result < battery:
            battery = result
    print('#{} {}'.format(tc, battery))
