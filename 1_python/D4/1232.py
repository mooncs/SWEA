# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산
def postorder(n):
    # 인덱스 범위가 벗어나면 반환
    if n > N:return
    if tree[n][1]:  # 왼쪽자식이 있다면
        postorder(tree[n][1])
    if tree[n][2]:  # 오른쪽자식이 있다면
        postorder(tree[n][2])
    # 사칙연산
    if tree[n][0] == '+':
        tree[n][0] = tree[tree[n][1]][0] + tree[tree[n][2]][0]
    elif tree[n][0] == '-':
        tree[n][0] = tree[tree[n][1]][0] - tree[tree[n][2]][0]
    elif tree[n][0] == '*':
        tree[n][0] = tree[tree[n][1]][0] * tree[tree[n][2]][0]
    elif tree[n][0] == '/':
        tree[n][0] = tree[tree[n][1]][0] / tree[tree[n][2]][0]

for tc in range(1, 11):
    # 노드의 총 수 N
    N = int(input())
    # [노드값, 왼쪽자식, 오른쪽자식]
    tree = [[0, 0, 0] for _ in range(N+1)]
    # 트리 정보 갱신
    for i in range(N):
        node_info = input().split()
        if len(node_info) == 4:
            tree[int(node_info[0])][0] = node_info[1]
            tree[int(node_info[0])][1] = int(node_info[2])
            tree[int(node_info[0])][2] = int(node_info[3])
        else:
            tree[int(node_info[0])][0] = int(node_info[1])
    postorder(1)
    print('#{} {}'.format(tc, int(tree[1][0])))

