# 4613. 러시아 국기 같은 깃발
T = int(input())
for tc in range(1, T+1):
    # N행 M열 깃발
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    min_cnt = 2500
    cnt_w = 0
    # 흰색이 아닌거 세고
    for w in range(0, N-2):
        for i in range(M):
            if flag[w][i] != 'W':
                cnt_w += 1
        # 파란색이 아닌거 세고
        cnt_b = 0
        for b in range(w+1, N-1):
            for j in range(M):
                if flag[b][j] != 'B':
                    cnt_b += 1
            # 빨간색이 아닌거 세서
            cnt_r = 0
            for r in range(b+1, N):
                for k in range(M):
                    if flag[r][k] != 'R':
                        cnt_r += 1
            # 바꿔야할 합이 제일 작은 것을 구한다.
            cnt = cnt_w + cnt_b + cnt_r
            if min_cnt > cnt:
                min_cnt = cnt

    print('#{} {}'.format(tc, min_cnt))
                
    