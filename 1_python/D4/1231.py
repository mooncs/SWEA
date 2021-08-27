# 1231. [S/W 문제해결 기본] 9일차 - 중위순회
def in_order():
    pass

for tc in range(1, 11):
    # 정점의 총 수 N
    N = int(input())
    # 정점의 알파벳
    arr = [0]*(N+1)
    # 정점의 왼쪽 자식
    left = [0]*(N+1)
    # 정점의 오른쪽 자식
    right = [0]*(N+1)

    for i in range(N):
        data = input()
        if len(data) == 7:
            i, n, l, r = data.split()
            arr[int(i)] = n
            left[int(i)] = int(l)
            right[int(i)] = int(r)
        elif len(data) == 5:
            i, n, l = data.split()
            arr[int(i)] = n
            left[int(i)] = int(l)
        else:
            i, n = data.split()
            arr[int(i)] = n
