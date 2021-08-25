# 11315. 오목 판정
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(input()) for _ in range(N)]
    # 하향, 우향, 우하향, 우상향
    drc = [[1,0],[0,1],[1,1],[-1,1]]
    flag = 'NO'
    for i in range(N):
        for j in range(N):
            if table[i][j] == 'o':
                for k in range(4):
                    cnt = 1
                    dr, dc = i+drc[k][0], j+drc[k][1]
                    while 0<=dr<N and 0<=dc<N and table[dr][dc]=='o':
                        cnt += 1
                        dr, dc = dr+drc[k][0], dc+drc[k][1]
                    if cnt >= 5:
                        flag = 'YES'
                        break
    
    print('#{} {}'.format(tc, flag))