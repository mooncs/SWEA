# 1953. [모의 SW 역량테스트] 탈주범 검거
from collections import deque

# def bfs():
#     # 상하좌우
#     drc = [[-1,0], [1,0], [0,-1], [0,1]]
#     conn = {
#         1:[[1,2,5,6], [1,2,4,7], [1,3,4,5], [1,3,6,7]],
#         2:[[1,2,5,6], [1,2,4,7], [], []],
#         3:[[], [], [1,3,4,5], [1,3,6,7]],
#         4:[[1,2,5,6], [], [], [1,3,6,7]],
#         5:[[], [1,2,4,7], [], [1,3,6,7]],
#         6:[[], [1,2,4,7], [1,3,4,5], []],
#         7:[[1,2,5,6], [], [1,3,4,5], []]
#     }
#     cnt = 1
#     while queue:
#         r, c = queue.popleft()
#         tcnt = visited[r][c] + 1
#         if tcnt > L:break
#         for d in range(4):
#             dr = r + drc[d][0]
#             dc = c + drc[d][1]
#             if dr < 0 or dr >= N or dc < 0 or dc >= M:continue
#             if visited[dr][dc] or not tunnel[dr][dc]:continue
#             if tunnel[dr][dc] in conn[tunnel[r][c]][d]:
#                 visited[dr][dc] = visited[r][c] + 1
#                 cnt += 1
#                 queue.append((dr, dc))
#     return cnt


# T = int(input())
# for tc in range(1, T+1):
#     # 지하 터널 지도의 세로 크기 N, 가로 크기 M
#     # 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C
#     # 탈출 후 소요된 시간 L
#     N, M, R, C, L = map(int, input().split())
#     tunnel = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0]*M for _ in range(N)]
#     queue = deque()
#     # 시작점 enqueue
#     queue.append((R, C))
#     visited[R][C] = 1
#     print('#{} {}'.format(tc, bfs()))


def bfs():
    # 상하좌우
    drc = [[-1,0], [1,0], [0,-1], [0,1]]
    # 상하좌우순으로 터널이 연결될 수 있는 터널 구조물 타입
    conn = {
        1:[[1,2,5,6], [1,2,4,7], [1,3,4,5], [1,3,6,7]],
        2:[[1,2,5,6], [1,2,4,7], [], []],
        3:[[], [], [1,3,4,5], [1,3,6,7]],
        4:[[1,2,5,6], [], [], [1,3,6,7]],
        5:[[], [1,2,4,7], [], [1,3,6,7]],
        6:[[], [1,2,4,7], [1,3,4,5], []],
        7:[[1,2,5,6], [], [1,3,4,5], []]
    }
    cnt, tcnt = 1, 2
    while tcnt <= L:
        # queue에 들어있는 수만큼 반복
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for d in range(4):
                dr = r + drc[d][0]
                dc = c + drc[d][1]
                if dr < 0 or dr >= N or dc < 0 or dc >= M:continue  # 좌표가 범위를 벗어나거나
                if visited[dr][dc] or not tunnel[dr][dc]:continue   # 방문했었거나 터널 구조물이 없을 경우 다음 방향 탐색
                if tunnel[dr][dc] in conn[tunnel[r][c]][d]:         # 위 조건을 통과하고 연결되는 터널 구조물일 경우
                    visited[dr][dc] = 1                             # 방문체크
                    cnt += 1                                        # 탈주범이 있을 수 있는 위치 +1
                    queue.append((dr, dc))                          # 다음 시간대의 시작점 enqueue
        tcnt += 1                                                   # queue가 다 돌았으면 time +1
    return cnt

T = int(input())
for tc in range(1, T+1):
    # 지하 터널 지도의 세로 크기 N, 가로 크기 M
    # 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C
    # 탈출 후 소요된 시간 L
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)] # 방문체크할 리스트
    queue = deque()
    queue.append((R, C))                # 시작점 enqueue
    visited[R][C] = 1                   # 시작점 방문체크
    print('#{} {}'.format(tc, bfs()))