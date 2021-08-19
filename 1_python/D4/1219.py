# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
def dfs(start, goal):
    # 방문 여부를 체크
    visited = [0]*100
    st=[]
    st.append(start)
    while st:
        for i in range():
            if graph[0][i] and not visited[graph[0][i]]:
                st.append(graph[0][i])
                pos = graph[0][i]
                visited[graph[0][i]] = 1
            




for _ in range(10):
    # 테스트 케이스 번호 tc, 길의 총 개수 n
    tc, n = map(int, input().split())
    # 연결관계를 담은 순서쌍
    op = list(map(int, input().split()))
    # 연결관계를 담을 리스트
    graph = [[0]*100 for _ in range(2)]
    # 연결관계를 2차원 리스트에 갱신
    for i in range(1, n*2, 2):
        if i % 4 == 1:
            graph[0][op[i-1]] = op[i]
        elif i % 4 == 3:
            graph[1][op[i-1]] = op[i]

    print(graph)




# # 1219. 길찾기
# def dfs(z,arr,c):
#     arr[c] = 1
#     while True:
#         if z[0][c] and not arr[z[0][c]]:
#             dfs(Z,arr,z[0][c])
#         elif z[1][c] and not arr[z[1][c]]:
#             dfs(Z,arr,z[1][c])
#         else:
#             break
#     return arr
 
 
# T = 10
# for _ in range(1, T + 1):
#     tc, num = map(int, input().split())
#     Z = [[0] * 100 for _ in range(2)]
#     route = list(map(int, input().split()))
#     for i in range(0,len(route), 2):
#         if not Z[0][route[i]]:
#             Z[0][route[i]] = route[i + 1]
#         else:
#             Z[1][route[i]] = route[i + 1]
#     visited = [0]*100
#     result = dfs(Z,visited,0)
#     print('#{} {}'.format(tc,result[-1]))