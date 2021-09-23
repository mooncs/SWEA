# 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합
def sumtree(idx):
    # 인덱스 범위를 벗어나면 0을 반환
    if idx > N:return 0
    # 노드에 값이 있다면 값을 반환
    if tree[idx]:return tree[idx]
    # 값이 없다면, 왼쪽 자식과 오른쪽 자식의 합을 재귀를 이용해 구한다.
    tree[idx] = sumtree(2*idx) + sumtree(2*idx+1)
    # 구한 값을 반환
    return tree[idx]

T = int(input())
for tc in range(1, T+1):
    # 노드의 개수 N, 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    N, M, L = map(int, input().split())
    # 트리 리스트
    tree = [0]*(N+1)
    # 입력 값을 받아 노드의 값을 갱신한다.
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v
    
    print('#{} {}'.format(tc, sumtree(L)))