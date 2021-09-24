# 1949. [모의 SW 역량테스트] 등산로 조성
def makeRoad(r, c, road, dig):
    global max_road
    # 가장 긴 등산로 길이 초기화
    if road > max_road:max_road = road
    # 좌표 이동, 상하좌우
    drc = [[-1,0], [1,0], [0,-1], [0,1]]
    for d in range(4):
        dr = r + drc[d][0]
        dc = c + drc[d][1]
        # 좌표가 범위를 벗어나거나 이미 방문했을 경우 다음 방향 탐색
        if dr < 0 or dr >= N or dc < 0 or dc >= N:continue
        if visited[dr][dc]:continue
        # 현재 봉우리 높이보다 이동할 봉우리의 높이가 낮을 경우
        if mountain[dr][dc] < mountain[r][c]:
            visited[dr][dc] = 1                     # 방문체크
            makeRoad(dr, dc, road+1, dig)
            visited[dr][dc] = 0                     # 방문체크 초기화
        # 공사가 가능하고 현재의 높이보다 공사한 다음의 높이가 낮을 경우
        elif dig and mountain[dr][dc]-K < mountain[r][c]:
            digged = mountain[dr][dc]               # 초기화를 위해 공사 전 높이 기록
            mountain[dr][dc] = mountain[r][c] - 1   # 공사진행
            visited[dr][dc] = 1                     # 방문체크
            makeRoad(dr, dc, road+1, False)
            visited[dr][dc] = 0                     # 방문체크 초기화
            mountain[dr][dc] = digged               # 공사 전 높이로 초기화

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # 한 변의 길이 N, 최대 공사 가능 깊이 K
    mountain = []                       # 봉우리 정보를 입력할 리스트
    max_h = 0                           # 가장 높은 봉우리 높이
    for _ in range(N):                  # 봉우리 정보 입력 및 최대 높이 갱신
        m = list(map(int, input().split()))
        if max_h < max(m):
            max_h = max(m)
        mountain.append(m)
    visited = [[0]*N for _ in range(N)] # 방문을 체크할 리스트
    max_road = 1                        # 가장 긴 등산로의 길이
    for r in range(N):
        for c in range(N):
            if mountain[r][c] == max_h: # 최대 높이일 떄 출발
                visited[r][c] = 1       # 방문체크
                makeRoad(r, c, 1, True) # 좌표, 등산로길이, 공사가능여부
                visited[r][c] = 0       # 방문체크 초기화
    print('#{} {}'.format(tc, max_road))


# # 오답 : 51개의 테스트케이스 중 50개가 맞았습니다.
# # 시작점 방문체크 초기화 미실시
# def makeRoad(r, c, road, dig):
#     global max_road
#     # 가장 긴 등산로 길이 초기화
#     if road > max_road:max_road = road
#     # 좌표 이동, 상하좌우
#     drc = [[-1,0], [1,0], [0,-1], [0,1]]
#     for d in range(4):
#         dr = r + drc[d][0]
#         dc = c + drc[d][1]
#         # 좌표가 범위를 벗어나거나 이미 방문했을 경우 다음 방향 탐색
#         if dr < 0 or dr >= N or dc < 0 or dc >= N:continue
#         if visited[dr][dc]:continue
#         # 현재 봉우리 높이보다 이동할 봉우리의 높이가 낮을 경우
#         if mountain[dr][dc] < mountain[r][c]:
#             visited[dr][dc] = 1                     # 방문체크
#             makeRoad(dr, dc, road+1, dig)
#             visited[dr][dc] = 0                     # 방문체크 초기화
#         # 공사가 가능하고 현재의 높이보다 공사한 다음의 높이가 낮을 경우
#         elif dig and mountain[dr][dc]-K < mountain[r][c]:
#             digged = mountain[dr][dc]               # 초기화를 위해 공사 전 높이 기록
#             mountain[dr][dc] = mountain[r][c] - 1   # 공사진행
#             visited[dr][dc] = 1                     # 방문체크
#             makeRoad(dr, dc, road+1, False)
#             visited[dr][dc] = 0                     # 방문체크 초기화
#             mountain[dr][dc] = digged               # 공사 전 높이로 초기화

# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())    # 한 변의 길이 N, 최대 공사 가능 깊이 K
#     mountain = []                       # 봉우리 정보를 입력할 리스트
#     max_h = 0                           # 가장 높은 봉우리 높이
#     for _ in range(N):                  # 봉우리 정보 입력 및 최대 높이 갱신
#         m = list(map(int, input().split()))
#         if max_h < max(m):
#             max_h = max(m)
#         mountain.append(m)
#     visited = [[0]*N for _ in range(N)] # 방문을 체크할 리스트
#     max_road = 1                        # 가장 긴 등산로의 길이
#     for r in range(N):
#         for c in range(N):
#             if mountain[r][c] == max_h: # 최대 높이일 떄 출발
#                 visited[r][c] = 1       # 방문체크
#                 makeRoad(r, c, 1, True) # 좌표, 등산로길이, 공사가능여부
#     print('#{} {}'.format(tc, max_road))