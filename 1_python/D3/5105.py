# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
def mazerunner():
    q = [[r,c,0]]
    # 상하좌우
    drc = [[-1,0], [1,0], [0,-1], [0,1]]
    while q:
        # 시작점의 위치
        pr, pc, t = q.pop(0)
        # 미로의 끝에 도착했다면, 이동거리를 리턴
        if maze[pr][pc] == 3:
            return t-1
        # 미로의 도착이 아니라면, 방문 표시
        maze[pr][pc] = 1
        # 4방향으로 모두 움직인다.
        for i in range(4):
            dr, dc = pr+drc[i][0], pc+drc[i][1]
            # 이동한 좌표가 범위내이고, 해당 좌표가 벽이 아니라면 q에 넣는다.
            if 0<=dr<N and 0<=dc<N and maze[dr][dc]!=1:
                q.append([dr,dc,t+1])
    # 다 돌아도 도착하지 않았다면, 미로를 탈출할 수 없음
    else:
        return 0
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                r,c = i,j

    print('#{} {}'.format(tc, mazerunner()))