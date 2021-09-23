# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색
def numbering(n):
    global num
    if n <= N:
        # 왼쪽 노드
        numbering(2*n)
        # 좌하단부터 numbering
        tree[n] = num
        num += 1
        # 오른쪽 노드
        numbering(2*n+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)    # 노드에 저장된 값을 저장할 리스트
    num = 1             # 저장할 값
    numbering(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))