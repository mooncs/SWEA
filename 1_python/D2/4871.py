# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
T = int(input())
for tc in range(1, T+1):
    # V개 이내의 노드를 E개의 간선으로 연결
    V, E = map(int, input().split())
    # 그래프 연결관계를 담을 빈 리스트(1번 노드부터 시작하기 때문에, 0번 index는 비워둘 예정)
    graph = [[0]*(V+1) for _ in range(V+1)]
    # 간선의 수 만큼 반복, 연결이 되어 있으면 1
    for _ in range(E):
        n1, n2 = map(int, input().split())
        # 방향성이 존재
        graph[n1][n2] = 1
    
    # 경로 확인, 출발 노드 S와 도착노드 G
    S, G = map(int, input().split())
    # 해당 노드를 지나갔는지 체크할 리스트
    chk =[0]*(V+1)
    # 현재의 이동경로를 담을 스택
    st = []
    while S!=G:
        for i in range(1, V+1):
            # 지나가지 않았고 노드가 연결되어있다면 해당 노드로 이동
            if graph[S][i] == 1 and chk[i]==0:
                # 현재 이동경로를 담고
                st.append(S)
                # 현재 위치 갱신
                S = i
                # 현재 위치를 지나갔다고 체크
                chk[S] = 1
                break
        else:
            # 지난 경로 중 다른 길이 없는지 탐색
            if st:
                S = st.pop()
            # 더이상 갈 곳이 없다면, 반복문 탈출
            else:
                break
                
    if S==G:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))


# T = int(input())
# for tc in range(1, T+1):
#     # V개 이내의 노드를 E개의 간선으로 연결
#     V, E = map(int, input().split())
#     # 그래프 연결관계를 담을 빈 리스트(1번 노드부터 시작하기 때문에, 0번 index는 비워둘 예정)
#     graph = [[0]*(V+1) for _ in range(V+1)]
#     # 간선의 수 만큼 반복, 연결이 되어 있으면 1
#     for _ in range(E):
#         n1, n2 = map(int, input().split())
#         # 방향성이 존재
#         graph[n1][n2] = 1
    
#     # 경로 확인, 출발 노드 S와 도착노드 G
#     S, G = map(int, input().split())
#     # 해당 노드를 지나갔는지 체크할 리스트
#     chk =[0]*(V+1)
#     # 현재의 이동경로를 담을 스택
#     st = []
#     # 현재의 위치
#     pos = S
#     while pos!=G:
#         for i in range(1, V+1):
#             # 지나가지 않았고 노드가 연결되어있다면 해당 노드로 이동
#             if graph[pos][i] == 1 and chk[i]==0:
#                 st.append(pos)
#                 pos = i
#                 chk[pos] = 1
#                 break
#         else:
#             if st:
#                 pos = st.pop()
#             else:
#                 break
                
#     if pos==G:
#         print('#{} 1'.format(tc))
#     else:
#         print('#{} 0'.format(tc))


# # 10개의 테스트케이스 중 6개 정답
# # 멍청이처럼 방향 고려X....문제를 잘 읽읍시다.
# T = int(input())
# for tc in range(1, T+1):
#     # V개 이내의 노드를 E개의 간선으로 연결
#     V, E = map(int, input().split())
#     # 그래프 연결관계를 담을 빈 리스트(1번 노드부터 시작하기 때문에, 0번 index는 비워둘 예정)
#     graph = [[0]*(V+1) for _ in range(V+1)]
#     # 간선의 수 만큼 반복, 연결이 되어 있으면 1
#     for _ in range(E):
#         n1, n2 = map(int, input().split())
#         graph[n1][n2] = graph[n2][n1] = 1
    
#     # 경로 확인, 출발 노드 S와 도착노드 G
#     S, G = map(int, input().split())
#     # 해당 노드를 지나갔는지 체크할 리스트
#     chk =[0]*(V+1)
#     # 현재의 이동경로를 담을 스택
#     st = []
#     # 현재의 위치
#     pos = S
#     while pos!=G:
#         for i in range(1, V+1):
#             # 지나가지 않았고 노드가 연결되어있다면 해당 노드로 이동
#             if graph[pos][i] == 1 and chk[i]==0:
#                 st.append(pos)
#                 pos = i
#                 chk[pos] = 1
#                 break
#         else:
#             if st:
#                 pos = st.pop()
#             else:
#                 break
                
#     if pos==G:
#         print('#{} 1'.format(tc))
#     else:
#         print('#{} 0'.format(tc))






# # 10개의 테스트케이스 중 6개 정답
# # 반례 5 4 1 2 1 3 1 4 1 5 1 5
# T = int(input())
# for tc in range(1, T+1):
#     # V개 이내의 노드를 E개의 간선으로 연결
#     V, E = map(int, input().split())
#     # 그래프 연결관계를 담을 빈 리스트(1번 노드부터 시작하기 때문에, 0번 index는 비워둘 예정)
#     graph = [[0]*(V+1) for _ in range(V+1)]
#     # 간선의 수 만큼 반복, 연결이 되어 있으면 1
#     for _ in range(E):
#         n1, n2 = map(int, input().split())
#         graph[n1][n2] = graph[n2][n1] = 1
    
#     # 경로 확인, 출발 노드 S와 도착노드 G
#     S, G = map(int, input().split())
#     # 해당 노드를 지나갔는지 체크할 리스트
#     chk =[0]*(V+1)
#     # 현재의 이동경로를 담을 스택
#     st = []
#     # 출발 지점은 지나간 것으로 체크
#     chk[S] = 1
#     st.append(S)
#     while S!=G:
#         for i in range(1, V+1):
#             # 지나가지 않았고 노드가 연결되어있다면 해당 노드로 이동
#             if chk[i]==0 and graph[S][i] == 1:
#                 chk[i] = 1
#                 st.append(i)
#                 S = i
#                 break
#         else:
#             if st:
#                 S = st.pop()
#             else:
#                 break
                
#     if S==G:
#         print('#{} 1'.format(tc))
#     else:
#         print('#{} 0'.format(tc))

    


