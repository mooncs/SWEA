# 10966. 물놀이를 가자
# # 오답 : 20개의 테스트케이스 중 4개가 맞았습니다. 제한시간 초과가 발생하였습니다.
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     # 방문체크를 할 리스트
#     visited = [[-1]*M for _ in range(N)]
#     queue = []
#     result = 0
#     for i in range(N):
#         bg = input()
#         for j in range(M):
#             # 물인 부분을 시작점으로 설정
#             if bg[j] == 'W':
#                 # 물인 부분을 0으로 표시해야 최소거리가 1부터 시작할 수 있다.
#                 visited[i][j] = 0
#                 queue.append((i, j))    
#     # 상하좌우
#     drc = [[-1,0], [1,0], [0,-1], [0,1]]
#     while queue:
#         r, c = queue.pop(0)
#         for d in range(4):
#             dr = r + drc[d][0]
#             dc = c + drc[d][1]
#             if 0<=dr<N and 0<=dc<M and visited[dr][dc]==-1:
#                 visited[dr][dc] = visited[r][c] + 1
#                 result += visited[dr][dc]
#                 queue.append((dr, dc))
    
#     print('#{} {}'.format(tc, result))


# # 오답 : 20개의 테스트케이스 중 4개가 맞았습니다. 제한시간 초과가 발생하였습니다.
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     # 방문체크를 할 리스트
#     visited = [[-1]*M for _ in range(N)]
#     queue = []
#     result = 0
#     for i in range(N):
#         bg = input()
#         for j in range(M):
#             # 물인 부분을 시작점으로 설정
#             if bg[j] == 'W':
#                 # 물인 부분을 0으로 표시해야 최소거리가 1부터 시작할 수 있다.
#                 visited[i][j] = 0
#                 queue.append((i, j))    
#     # 상하좌우
#     drc = [[-1,0], [1,0], [0,-1], [0,1]]
#     while queue:
#         r, c = queue.pop(0)
#         for d in range(4):
#             dr = r + drc[d][0]
#             if dr < 0 or dr >= N:continue
#             dc = c + drc[d][1]
#             if dc < 0 or dc >= M:continue
#             if visited[dr][dc] != -1:continue

#             visited[dr][dc] = visited[r][c] + 1
#             result += visited[dr][dc]
#             queue.append((dr, dc))
    
#     print('#{} {}'.format(tc, result))


# # 오답 : 20개의 테스트케이스 중 4개가 맞았습니다. 제한시간 초과가 발생하였습니다.
# def bfs():
#     result = 0
#     while queue:
#         r, c = queue.pop(0)
#         for d in range(4):
#             dr = r + drc[d][0]
#             if dr < 0 or dr >= N:continue
#             dc = c + drc[d][1]
#             if dc < 0 or dc >= M:continue
#             if visited[dr][dc] != -1:continue

#             visited[dr][dc] = visited[r][c] + 1
#             result += visited[dr][dc]
#             queue.append((dr, dc))
#     return result

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     # 방문체크를 할 리스트
#     visited = [[-1]*M for _ in range(N)]
#     queue = []
#     result = 0
#     for i in range(N):
#         bg = input()
#         for j in range(M):
#             # 물인 부분을 시작점으로 설정
#             if bg[j] == 'W':
#                 # 물인 부분을 0으로 표시해야 최소거리가 1부터 시작할 수 있다.
#                 visited[i][j] = 0
#                 queue.append((i, j))    
#     # 상하좌우
#     drc = [[-1,0], [1,0], [0,-1], [0,1]]
#     print('#{} {}'.format(tc, bfs()))


from collections import deque

def bfs():
    # 상하좌우
    drc = [[-1,0], [1,0], [0,-1], [0,1]]
    result = 0
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            dr = r + drc[d][0]
            if dr < 0 or dr >= N:continue
            dc = c + drc[d][1]
            if dc < 0 or dc >= M:continue
            if visited[dr][dc] != -1:continue

            visited[dr][dc] = visited[r][c] + 1
            result += visited[dr][dc]
            queue.append((dr, dc))
    return result

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 방문체크를 할 리스트
    visited = [[-1]*M for _ in range(N)]
    queue = deque()
    for i in range(N):
        bg = input()
        for j in range(M):
            # 물인 부분을 시작점으로 설정
            if bg[j] == 'W':
                # 물인 부분을 0으로 표시해야 최소거리가 1부터 시작할 수 있다.
                visited[i][j] = 0
                queue.append((i, j))    
    print('#{} {}'.format(tc, bfs()))