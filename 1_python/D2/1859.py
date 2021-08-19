# 1859. 백만 장자 프로젝트
T = int(input())
for tc in range(1, T+1):
    # N일 동안의 물건의 매매가를 예측
    N = int(input())
    # N일 동안의 매매가
    price = list(map(int, input().split()))
    # 제일 마지막 날을 기준
    max_price = price[-1]
    # 최종적으로 벌 돈 money와 구매한 원료의 수 cnt
    money, cnt = 0, 0
    for i in range(N-2, -1, -1):
        # 탐색 가격이 max_price보다 작으면 구매하고 가격만큼 money 감소
        if price[i] < max_price:
            money -= price[i]
            cnt += 1
        # 탐색 가격이 max_price보다 크거나 같으면 지금까지 구매했던 원료를 현재의 max_price로 판매
        elif price[i] >= max_price:
            money += max_price*cnt
            # 원료의 수 갱신
            cnt = 0
            # max_price 갱신
            max_price = price[i]
    # 첫 날까지 다 검색했으면 한 번더 현재까지의 가격 계산
    money += max_price*cnt
        
    print('#{} {}'.format(tc, money))
    

# # error ===> bad gateway
# def SelectionSort(arr):
#     for i in range(len(arr)-1):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         arr[min_idx], arr[i] = arr[i], arr[min_idx]
#     return arr

# T = int(input())
# for tc in range(1, T+1):
#     # N일 동안의 물건의 매매가를 예측
#     N = int(input())
#     price = list(map(int, input().split()))
#     sort_price = SelectionSort(price[::])

#     max_idx = N-1
#     sell, buy, cnt = 0, 0, 0
#     while price:
#         if price[0] == sort_price[max_idx]:
#             price.pop(0)
#             max_idx -= 1
#         else: 
#             break
    
#     for i in range(len(price)):
#         if price[i] < sort_price[max_idx]:
#             buy += price[i]
#             cnt += 1
#         elif price[i] == sort_price[max_idx]:
#             sell += price[i]*cnt - buy
#             buy = 0
#             cnt = 0
#             max_idx -= 1

#     print('#{} {}'.format(tc, sell))
        
