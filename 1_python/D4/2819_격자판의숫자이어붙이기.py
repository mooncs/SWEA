# 2819. 격자판의 숫자 이어 붙이기
def dfs(r, c, idx, result):
    drc = [[-1,0],[1,0],[0,-1],[0,1]]   # 상하좌우 이동
    result += grid[r][c]                # 격자판 숫자 이어 붙이기
    if idx == 6:                        # 이은 숫자의 길이가 7이면
        answer.add(result)              # 결과 set에 저장
        return
    for i in range(4):                  # 4방향 모두로 이동
        dr = r + drc[i][0]              # 행 갱신
        dc = c + drc[i][1]              # 열 갱신
        if 0<=dr<4 and 0<=dc<4:         # 행과 열이 범위 내에 있으면
            dfs(dr, dc, idx+1, result)  # 해당 행과 열로 이동하여 재귀시행

for tc in range(1, int(input())+1):
    grid = [input().split() for _ in range(4)]
    answer = set()                      # 7자리 숫자를 담을 set
    for r in range(4):                  # 모든 격자판을 돌면서 반복
        for c in range(4):
            dfs(r, c, 0, '')
    print('#{} {}'.format(tc, len(answer)))