# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
def dfs(start, goal):
    # 방문 여부를 체크
    visited = [0]*100
    st=[]
    st.append(start)
    while st:
        top = st.pop()
        if top==goal:
            return 1
        visited[top] = 1
        for g in graph[top]:
            if not visited[g]:
                st.append(g)
    return 0
            
for _ in range(10):
    # 테스트 케이스 번호 tc, 길의 총 개수 n
    tc, n = map(int, input().split())
    # 연결관계를 담은 순서쌍
    op = list(map(int, input().split()))
    # 연결관계를 담을 리스트
    graph = [[] for _ in range(100)]
    # 연결관계를 표시
    for i in range(0, n*2, 2):
        graph[op[i]].append(op[i+1])

    print('#{} {}'.format(tc, dfs(0, 99)))