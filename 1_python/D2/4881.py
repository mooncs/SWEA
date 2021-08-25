# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합
def sel_sum(idx, total):
    global min_sum
    # 배열의 깊이만큼 갔으면
    if idx == N:
        if total < min_sum:
            min_sum = total
        return
    # 현재까지 더해진 것이 최소합보다 크거나 같다면 더이상 구할 필요 없다.
    if total >= min_sum:
        return

    for j in range(N):
        # 해당 column의 수를 선택하지 않았다면
        if check[j]:
            # 선택했음을 체크
            check[j] = False
            # 다음줄 탐색
            sel_sum(idx+1, total+arr[idx][j])
            # 초기화
            check[j] = True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # NxN 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최소합, 10보다 작은 자연수->최대값 9, 3≤N≤10->최대값 10 => 최대 90
    min_sum = 90
    # 앞 줄에서 선택한 column을 체크할 리스트
    check = [True for _ in range(N)]

    sel_sum(0, 0)

    print('#{} {}'.format(tc, min_sum))


##################################################################################################
# 10개의 테스트케이스 중 6개
# 제한시간 초과가 발생하였습니다. 제한시간 초과로 전체 혹은 일부 테스트 케이스는 채점이 되지 않을 수 있습니다.
# def sel_sum(idx, total):
#     global min_sum
#     # 배열의 깊이만큼 갔으면
#     if idx == N:
#         if total < min_sum:
#             min_sum = total
#         return

#     for j in range(N):
#         # 해당 column의 수를 선택하지 않았다면
#         if check[j]:
#             # 선택했음을 체크
#             check[j] = False
#             # 다음줄 탐색
#             sel_sum(idx+1, total+arr[idx][j])
#             # 초기화
#             check[j] = True


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     # NxN 배열
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # 최소합, 10보다 작은 자연수->최대값 9, 3≤N≤10->최대값 10 => 최대 90
#     min_sum = 90
#     # 앞 줄에서 선택한 column을 체크할 리스트
#     check = [True for _ in range(N)]

#     sel_sum(0, 0)

#     print('#{} {}'.format(tc, min_sum))



    