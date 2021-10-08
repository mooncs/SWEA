# 2806. N-Queen
def nQueen(idx):
    global cnt
    # 모든 행에 Queen을 다 놓았다면
    if idx == n:cnt += 1
    # 0~n-1열까지 반복
    for c in range(n):
        # 이전 행 탐색
        for r in range(idx):
            # 이전 행의 열과 현재 열이 같다면 중단
            if check[r] == c:break
            # 대각선 위치라면 중단
            if abs(idx-r) == abs(c-check[r]):break
        # for문이 정상적으로 돌았다면, 같은 열과 대각선에 위치하지 않은 것이므로
        else:
            # 해당 행의 열을 표시
            check[idx] = c
            # 다음 행 탐색
            nQueen(idx+1)
            # 원상 복구
            check[idx] = -1

for tc in range(1, int(input())+1):
    n = int(input())
    check = [-1]*n  # 인덱스 행에 Queen이 위치한 열 표시
    cnt = 0         # 경우의 수를 count할 변수
    nQueen(0)       # Queen 위치하기
    print('#{} {}'.format(tc, cnt))