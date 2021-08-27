# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
# 오답 : 10개의 테스트케이스 중 8개가 맞았습니다.
# f = q.pop() -> f = q.pop(0) 수정
def BFS(s, g):
    visited = [-1]*(V+1)                    # visited 생성
    q = [s]                                 # 큐생성
    visited[s] = 0                          # 방문 표시
    while q:            
        f = q.pop(0)                        # 큐의 제일 앞을 pop
        if f == g:                          # 도착 노드에 도착했으면
            return visited[g]               # visited에 담긴 거리를 출력
        for n in adjList[f]:                # 현재 노드와 연결된 노드 중
            if visited[n] == -1:            # 아직 방문하지 않은 노드일 경우
                q.append(n)                 # 큐에 넣어주고
                visited[n] = visited[f]+1   # 거리를 측정하기 위해, visited에 거리 입력
    return 0

# def BFS2():
#     Q = [S]
#     visited = [False] * (V+1)
#     visited[S] = True
#     dist = 0
#     while Q:
#         size = len(Q)
#         # Q size로 묶어서 현재 같은 레벨의 친구들만 돈다.
#         for _ in range(size):
#             v = Q.pop(0)

#             if v == G: return dist

#             for i in range(1, V+1):
#                 if visited[i] == False and adj_arr[v][i] == 1:
#                     Q.append(i)
#                     visited[i] = True
#         dist += 1
#     return 0

T = int(input())
for tc in range(1, T+1):
    # V개의 노드, E개의 간선
    V, E = map(int, input().split())
    # 인접 리스트
    adjList = [[] for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        # 방향이 없는
        adjList[i].append(j)
        adjList[j].append(i)
    # 출발 노드 S, 도착 노드 G
    S, G = map(int, input().split())

    print('#{} {}'.format(tc, BFS(S, G)))