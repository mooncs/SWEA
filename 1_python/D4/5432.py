# 5432. 쇠막대기 자르기
# ★★★★, idea참고
T = int(input())
for tc in range(1, T+1):
    data = list(input())
    # 먼저 레이저 표시하기
    for i in range(len(data)):
        # '('다음에 바로 ')'가 오면 레이저이므로 '('자리를 'L'로 ')'자리는 공백으로 교체
        if data[i]=='(' and data[i+1]==')':
            data[i] = 'L'
            data[i+1] = ' '

    stick = 0   # 현재 생성된 막대 수
    laser = 0   # 잘라진 막대수
    for d in data:
        # '(' 나오면 그자리부터 막대가 하나씩 생긴다.
        # 레이저를 한 번 맞으면 막대는 1이 아니라 2개로 생성되는 것이므로, 기본적으로 1개는 생성된다.
        if d == '(':
            stick += 1
            laser += 1
        # 'L', 레이저 위치가 나오면 현재까지 생성된 막대가 잘라져서 막대 수가 하나씩 증가한다.
        elif d == 'L':
            laser += stick
        # ')'가 나오면 그자리까지가 막대임으로 막대기 제거
        elif d == ')':
            stick -= 1

    print('#{} {}'.format(tc, laser))