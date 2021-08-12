# 2001. 파리 퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            kill = 0
            for i in range(M):
                for j in range(M):
                    kill += flies[r+i][c+j]
            if kill > max_kill:
                max_kill = kill
    print('#{} {}'.format(tc, max_kill))