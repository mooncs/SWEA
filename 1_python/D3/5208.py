# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2
for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    n, battery = arr[0], arr[1:]
    dp = [-1]*n
    for i in range(n-1):
        for j in range(1, battery[i]+1):
            if i+j >= n:
                break
            if dp[i+j] == -1:
                dp[i+j] = dp[i] + 1
            else:
                dp[i+j] = min(dp[i]+1, dp[i+j])
    print('#{} {}'.format(tc, dp[-1]))


# # dfs활용
# def dfs(pos, charge):
#     global min_charge
#     # 현재 교환횟수가 최소 교환횟수보다 커지면 중단
#     if min_charge < charge:
#         return
#     # 목적지에 도착했을때, 교환횟수를 기록
#     if pos >= goal:
#         min_charge = charge
#         return
#     # 제일 많이 이동할 수 있는 거리부터 탐색
#     for dist in range(battery[pos], 0, -1):
#         dfs(pos+dist, charge+1)

# for tc in range(1, int(input())+1):
#     arr = list(map(int, input().split()))
#     # 목적지, 정류장별 배터리
#     goal, battery = arr[0]-1, arr[1:]
#     # 최소 교환횟수
#     min_charge = 100
#     # 출발지 교환은 교환횟수에 포함하지 않기 때문에 -1에서 시작
#     dfs(0, -1)
#     print('#{} {}'.format(tc, min_charge))


# # 오답 : 10개의 테스트케이스 중 5개가 맞았습니다.
# for tc in range(1, int(input())+1):
#     arr = list(map(int, input().split()))
#     goal = arr[0]-1
#     move = arr[1]
#     charge = arr[2:]
#     cnt = 0
#     while move < goal:
#         if move + charge[0] > goal:
#             cnt += 1
#             break
#         move += charge[move-1]
#         cnt += 1
#         if move > goal:
#             break

#     print('#{} {}'.format(tc, cnt))