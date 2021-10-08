# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색
def bSearch(x):
    global cnt
    min_i, max_i = 0, n-1
    direction = []
    while min_i <= max_i:
        mid = (min_i+max_i)//2
        if A[mid] == x:
            cnt += 1
            break
        elif A[mid] > x:
            max_i = mid-1
            if direction and direction[-1]=='l':break
            direction.append('l')
        else:
            min_i = mid+1
            if direction and direction[-1]=='r':break
            direction.append('r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for b in B:
        bSearch(b)
    print('#{} {}'.format(tc, cnt))


# for tc in range(1, int(input())+1):
#     n, m = map(int, input().split())
#     A = sorted(list(map(int, input().split())))
#     B = list(map(int, input().split()))
#     cnt = 0
#     for b in B:
#         min_i, max_i = 0, n-1
#         direction = []
#         while min_i <= max_i:
#             mid = (min_i+max_i)//2
#             if A[mid] == b:
#                 cnt += 1
#                 break
#             elif A[mid] > b:
#                 max_i = mid-1
#                 if direction and direction[-1]=='l':break
#                 direction.append('l')
#             else:
#                 min_i = mid+1
#                 if direction and direction[-1]=='r':break
#                 direction.append('r')
#     print('#{} {}'.format(tc, cnt))