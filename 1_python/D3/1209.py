# 1209. [S/W 문제해결 기본] 2일차 - Sum

# 대소 비교 함수
def my_max(a, b):
    if a > b: return a
    return b

for _ in range(1, 11):
    tc = int(input())
    # 100x100행렬 만들기
    numbers = [list(map(int, input().split())) for _ in range(100)]
    # max_sum : 최대 합
    # dr_sum : 우하향 대각선 합
    # dl_sum : 좌하향 대각선 합
    max_sum = 0
    dr_sum = 0
    dl_sum = 0
    for r in range(100):
        dr_sum += numbers[r][r]
        dl_sum += numbers[r][99-r]
        # r_sum : 행의 합
        # c_sum : 열의 합
        r_sum = 0
        c_sum = 0
        for c in range(100):
            r_sum += numbers[r][c]
            c_sum += numbers[c][r]
        # 최대 합 갱신
        if my_max(r_sum, c_sum) > max_sum:
            max_sum = my_max(r_sum, c_sum)
    if my_max(dr_sum, dl_sum) > max_sum:
            max_sum = my_max(dr_sum, dl_sum)

    print('#{} {}'.format(tc, max_sum))