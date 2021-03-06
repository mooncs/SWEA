# 1226. [S/W 문제해결 기본] 7일차 - 미로1
for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    drc = [[-1,0], [0,-1], [1,0], [0,1]]
    q = [[1, 1]]
    possible = 0
    while q:
        # 현재 위치
        pos = q.pop(0)
        r, c = pos[0], pos[1]
        # 현 위치의 값이 3일 경우 종료
        if maze[r][c] == 3:
            possible = 1
            break
        # 미로가 막혀있지 않다면 방문 표시
        maze[r][c] = 1
        # 현 위치에서 상하좌우로 이동했을때
        for i in range(4):
            dr, dc = r+drc[i][0], c+drc[i][1]
            # 좌표가 범위 안에 있고, 벽이 아니라면
            if 0<=dr<16 and 0<=dc<16 and maze[dr][dc]!=1:
                q.append([dr, dc])
    
    print('#{} {}'.format(tc, possible))



##########################################################################
# for _ in range(10):
    # tc = int(input())
    # maze = [list(map(int, input())) for _ in range(16)]
    # dr = [-1, 0, +1, 0]
    # dc = [0, -1, 0, +1]
    # stack = [[1, 1]]
    # possible = 0
    # while stack:
    #     # 현재 위치
    #     pos = stack.pop()
    #     r, c = pos[0], pos[1]
    #     # 미로가 막혀있으면 돌아가기
    #     if maze[r][c] == 1:
    #         continue
    #     # 현 위치의 값이 3일 경우 종료
    #     elif maze[r][c] == 3:
    #         possible = 1
    #         break
    #     # 미로가 막혀있지 않다면 방문 표시
    #     maze[r][c] = 1
    #     # 현 위치에서 상하좌우 위치 stack에 push
    #     if 0<r<15 and 0<c<15:
    #         for i in range(4):
    #             stack.append([r+dr[i], c+dc[i]])
    
    # print('#{} {}'.format(tc, possible))



    