# 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree
def counting(x):
    global count
    # 노드가 없으면 return
    if x == 0:return
    # 노드가 있으면 카운팅
    count += 1
    counting(tree[x][0])    # 왼쪽자식
    counting(tree[x][1])    # 오른쪽자식

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    conn = list(map(int, input().split()))
    # tree를 만들 빈 리스트, [왼쪽자식, 오른쪽자식]
    tree = [[0, 0] for _ in range(E+2)]
    # 트리 만들기
    for i in range(0, len(conn), 2):
        # 왼쪽자식이 없다면
        if not tree[conn[i]][0]:
            tree[conn[i]][0] = conn[i+1]
        # 왼쪽자식이 있다면
        else:
            tree[conn[i]][1] = conn[i+1]
    count = 0   # 서브트리의 노드 개수
    counting(N)
    print('#{} {}'.format(tc, count))
        