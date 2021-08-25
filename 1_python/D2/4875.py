# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
    # 출발 위치 스택에 push
    stack = [[r, c]]
    # 상, 우, 하, 좌
    drc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 도착하는 경로가 존재하는지 확인
    possible = 0 
    while stack:
        # 현 위치
        pos = stack.pop()
        pr, pc = pos[0], pos[1]
        # 목적지에 도착하였다면, 경로가 존재한다고 표시하고, 반복문 탈출
        if maze[pr][pc] == 3:
            possible = 1
            break
        # 막혀있지도 도착하지도 않았다면, 현 위치 방문표시
        maze[pr][pc] = 1
        # 이동할 수 있는 모든 방향 체크
        for i in range(4):
            dr, dc = pr+drc[i][0], pc+drc[i][1]
            # 행과 열 범위안에 있고 방문하지 않은(벽이 아닌) 곳이라면 스택에 push
            if 0<=dr<N and 0<=dc<N and maze[dr][dc] != 1:
                stack.append([dr, dc])

    print('#{} {}'.format(tc, possible))

##########################################################################################
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(map(int, list(input()))) for _ in range(N)]
#     # 출발점 찾기
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 r, c = i, j
#     # 출발 위치 스택에 push
#     stack = [[r, c]]
#     # 상, 우, 하, 좌
#     drc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
#     # 도착하는 경로가 존재하는지 확인
#     possible = 0 
#     while stack:
#         # 현 위치
#         pos = stack.pop()
#         pr, pc = pos[0], pos[1]
#         # 미로가 막혀있으면 돌아가기
#         if maze[pr][pc] == 1:
#             continue
#         # 목적지에 도착하였다면, 경로가 존재한다고 표시하고, 반복문 탈출
#         elif maze[pr][pc] == 3:
#             possible = 1
#             break
#         # 막혀있지도 도착하지도 않았다면, 현 위치 방문표시
#         maze[pr][pc] = 1
#         # 이동할 수 있는 모든 방향 체크
#         for i in range(4):
#             dr, dc = pr+drc[i][0], pc+drc[i][1]
#             # 행과 열 범위안에 있고 방문하지 않은(벽이 아닌) 곳이라면 스택에 push
#             if 0<=dr<N and 0<=dc<N and maze[dr][dc] != 1:
#                 stack.append([dr, dc])

#     print('#{} {}'.format(tc, possible))


    