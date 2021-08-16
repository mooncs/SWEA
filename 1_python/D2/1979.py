# 1979. 어디에 단어가 들어갈 수 있을까

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0     # 단어 길이와 빈칸의 수가 동일한 것 카운트
    row = 0     # 행에서 1의 개수 카운트
    col = 0     # 열에서 1의 개수 카운트
    # tp로 방향 체크
    for i in range(N):
        for j in range(N):
            # 가로로 검색
            if puzzle[i][j] == 1:
                row += 1 
            else:               # 행이 1이 아닐때,
                if row == K:    # 이전까지 연속된 1의 수가 K와 동일하다면 cnt 카운트
                    cnt += 1
                row = 0         # 더 이상 연속된 것이 아니기 때문에 행 카운트 초기화

            # 세로로 검색
            if puzzle[j][i] == 1:
                col += 1
            else:               # 열이 1이 아닐때,
                if col == K:    # 이전까지 연속된 1의 수가 K와 동일하다면 cnt 카운트
                    cnt += 1    # 더 이상 연속된 것이 아니기 때문에 열 카운트 초기화
                col = 0
        if row == K:            # 행에서 중간에 0 없이 연속된 1의 수가 K와 동일하다면,
            cnt += 1            # cnt 카운트
            row = 0             # 행 카운트 초기화
        else: row = 0           # 연속된 수가 K보다 크거나 작아도 카운트 초기화
        if col ==K:             # 열에서 중간에 0 없이 연속된 1의 수가 K와 동일하다면,
            cnt += 1            # cnt 카운트
            col = 0             # 열 카운트 초기화
        else: col = 0           # 연속된 수가 K보다 크거나 작아도 카운트 초기화

    print('#{} {}'.format(tc, cnt))