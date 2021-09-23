# 1231. [S/W 문제해결 기본] 9일차 - 중위순회
# 중위순휘함수 LVR
def in_order(T):
    global ans
    if arr[T]:              # 정점이 존재하면
        in_order(left[T])   # 정점의 왼쪽 자식으로
        ans += arr[T]       # 정점에서 할 일, 정답 문자열에 현 정점의 알파벳 추가
        in_order(right[T])  # 정점의 오른쪽 자식으로

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
        # 입력된 데이터의 길이에 따라 다른 작업
        # 정점번호i, 정점의 알파벳n, 정점의 왼쪽 자식l, 정점의 오른쪽 자식 r
        data = input().split()
        if len(data) == 4:
            i, n, l, r = data[0], data[1], data[2], data[3]
            arr[int(i)] = n
            left[int(i)] = int(l)
            right[int(i)] = int(r)
        elif len(data) == 3:
            i, n, l = data[0], data[1], data[2]
            arr[int(i)] = n
            left[int(i)] = int(l)
        else:
            i, n = data[0], data[1]
            arr[int(i)] = n
    ans = ''    # 정답을 담을 문자열
    in_order(1) # 중위순회
    print('#{} {}'.format(tc, ans))
