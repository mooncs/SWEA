# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
def mazerunner():
    q = [[r,c,0]]
    # 상하좌우
    drc = [[-1,0], [1,0], [0,-1], [0,1]]
    while q:
        pr, pc, t = q.pop(0)
        if maze[pr][pc] == 3:
            return t-1
        maze[pr][pc] = 1
        for i in range(4):
            dr, dc = pr+drc[i][0], pc+drc[i][1]
            if 0<=dr<N and 0<=dc<N and maze[dr][dc]!=1:
                q.append([dr,dc,t+1])
    else:
        return 0
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                r,c = i,j

    print('#{} {}'.format(tc, mazerunner()))