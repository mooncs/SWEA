# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기

T = int(input())
for tc in range(1, T+1):
    # 칠할 영역의 개수
    N = int(input())
    # 10*10, 색이 칠해지지 않은 상태
    base = [[0]*10 for _ in range(10)]
    # 보라색 카운트
    cnt = 0
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # 행이동
        for r in range(r1, r2+1):
            # 열이동
            for c in range(c1, c2+1):
                # 색이 칠해져있지 않거나 다른 색이 칠해져 있다면, 해당 색의 수를 더한다.
                if base[r][c] != color:
                    base[r][c] += color
                # 색칠된 수가 3이면 보라색이기 때문에, 보라색 카운트 증가시킨다.
                if base[r][c] == 3:
                    cnt += 1

    print('#{} {}'.format(tc, cnt))