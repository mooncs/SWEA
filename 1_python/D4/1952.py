# 1952. [모의 SW 역량테스트] 수영장
for tc in range(1, int(input())+1):
    d, m, ms, y = map(int, input().split())     # 1일, 1달, 3달, 1년 이용권
    plan = list(map(int, input().split()))      # 1월부터 12월까지의 이용 계획
    cost = [0]*13                               # 비용의 누적합을 담을 리스트
    cost[1] = min(d*plan[0], m)                 # 1월 1일권과 1달권 비용 중 저렴한 것 이용
    cost[2] = cost[1] + min(d*plan[1], m)       # 2월 또한 마찬가지로 구하고, 이전달에 누적합
    for i in range(3, 13):                      # 3월~12월
        cost[i] = min(cost[i-3] + ms, cost[i-1] + min(d*plan[i-1], m))
    print('#{} {}'.format(tc, min(y, cost[12])))# 1년권과 마지막 누적합 비교


# def swim(idx, cost):
#     global min_cost
#     if idx > 11:                                            # 12달 다 계산했으면
#         if cost < min_cost:min_cost = cost                  # 최소 비용 갱신
#         return
    
#     if plan[idx]:                                           # 해당 월 이용계획이 있으면
#         for i in range(3):
#             if i == 0:swim(idx+1, cost+plan[idx]*fees[i])   # 1일권
#             elif i == 1:swim(idx+1, cost+fees[i])           # 1달권
#             else:swim(idx+3, cost+fees[i])                  # 3달권
#     else:swim(idx+1, cost)                                  # 이용계획이 없다면 다음 달 탐색
            
# T = int(input())
# for tc in range(1, T+1):
#     fees = list(map(int, input().split()))  # 1일, 1달, 3달, 1년 이용권
#     plan = list(map(int, input().split()))  # 1월부터 12월까지의 이용 계획
#     min_cost = fees[3]                      # 1년 이용가격
#     swim(0, 0)
#     print('#{} {}'.format(tc, min_cost))