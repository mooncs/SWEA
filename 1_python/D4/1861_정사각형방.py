# 1861. 정사각형 방
from collections import deque

def bfs():
    max_move = 0
    drc = [[-1,0],[1,0],[0,-1],[0,1]]
    for r in range(n):
        for c in range(n):
            q = deque()
            q.append((r, c, 1))
            while q:
                cr, cc, move = q.popleft()
                for i in range(4):
                    dr = cr+drc[i][0]
                    dc = cc+drc[i][1]
                    if 0<=dr<n and 0<=dc<n and square[dr][dc]-square[cr][cc]==1:
                        q.append((dr,dc,move+1))
                        break
            if move > max_move:
                max_move = move
                room = square[r][c]
            elif move == max_move:
                room = min(room, square[r][c])
    return room, max_move

for tc in range(1, int(input())+1):
    n = int(input())
    square = [list(map(int, input().split())) for _ in range(n)]
    room, max_move = bfs()
    print('#{} {} {}'.format(tc, room, max_move))


############################################################################################
# check!!!!!!!!!!!!!!!!!!!!!!
# T = int(input())
# drc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
# for tc in range(1, T+1):
#     N = int(input())
#     room = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[False]*N for _ in range(N)]
#     room_list = set()
#     for r in range(N):
#         for c in range(N):
#             if visited[r][c]:
#                 continue
 
#             stack = [(r, c)]
#             temp = set()
#             while stack:
#                 _r, _c  = stack.pop()
#                 visited[_r][_c] = True   
#                 temp.add(room[_r][_c])
#                 for dr, dc in drc:
#                     nr = _r + dr
#                     nc = _c + dc
#                     if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
#                         if room[_r][_c] + 1 == room[nr][nc] or room[_r][_c] - 1 == room[nr][nc]:
#                             stack.append((nr, nc))
 
#             if len(room_list) < len(temp):  # 가장 많은 방을 이동할수 있는 경우
#                 room_list = temp
             
#             elif len(room_list) == len(temp):   # 카운트가 같은 경우
#                 if min(room_list) > min(temp):  # 방번호가 더 작은 방을 저장
#                     room_list = temp
 
#     print('#{} {} {}'.format(tc, min(room_list), len(room_list)))


# # 오답 : 27개의 테스트케이스 중 14개가 맞았습니다.
# def cntRoom():
#     max_cnt = 1
#     room = N**2
#     drc = [[-1,0],[1,0],[0,-1],[0,1]]       # 상하좌우 이동
#     for i in range(N):
#         for j in range(N):
#             cnt = 1
#             q = [(i, j)]
#             while q:
#                 pr, pc = q.pop()    
#                 for k in range(4):
#                     dr, dc = pr+drc[k][0], pc+drc[k][1]
#                     if 0<=dr<N and 0<=dc<N and sq[dr][dc]-sq[pr][pc]==1:
#                         q.append((dr, dc))
#                         cnt += 1
#             if cnt>max_cnt:
#                 max_cnt = cnt
#                 room = sq[i][j]
#             elif cnt == max_cnt :
#                 if room>sq[i][j]:
#                     room = sq[i][j]
#     return max_cnt, room

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     sq = [list(map(int, input().split())) for _ in range(N)]# N²개의 방
#     max_cnt, room = cntRoom()
#     print('#{} {} {}'.format(tc, room, max_cnt))
    