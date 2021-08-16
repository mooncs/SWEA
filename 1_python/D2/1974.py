# 1974. 스도쿠 검증
# 사각형 확인 함수
def chk_square(sdoku, c):
    number = []
    for i in range(3):
        for j in range(3):
            if sdoku[i][j+c] in number:
                return 0
            else:
                number.append(sdoku[i][j+c])
    return 1

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    
    for i in range(9):
        row, col, square = 0, 0, 0
        for j in range(9):
            # 3*3사각형은 index가 0, 3, 6일때만 검사하면 된다.
            if i % 3 == 0 and j % 3 ==0:
                square += chk_square(sudoku[i:i+3], j)
            row += sudoku[i][j]
            col += sudoku[j][i]
        # index가 0, 3, 6일 때, 1~9까지의 수가 겹치지 않은 사각형이 3개가 안된다면
        # (j는 8까지 다 돌고 나온상태라 조건을 걸 필요 없다.)
        if i % 3 == 0 and square != 3:
            # 스도쿠 퍼즐이 아니므로 0을 출력하고 반복문 탈출
            print('#{} 0'.format(tc))
            break
        # 행과 열의 합이 45가 되지 않는다면, 스도쿠 퍼즐이 아니므로 0을 출력하고 반복문 탈출
        if row != 45 or col != 45:
            print('#{} 0'.format(tc))
            break
    # 반복문이 문제 없이 잘 돌았다면 스도쿠이므로 1 출력
    else:
        print('#{} 1'.format(tc))


# flag 사용
def chk_square(sdoku, c):
    number = []
    for i in range(3):
        for j in range(3):
            if sdoku[i][j+c] not in number:
                number.append(sdoku[i][j+c])
    if len(number) != 9:
        return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    flag = False
    for i in range(9):
        if flag:
            break
        row, col = 0, 0
        for j in range(9):
            if i % 3 == 0 and j % 3 ==0:
                flag = chk_square(sudoku[i:i+3], j)
            row += sudoku[i][j]
            col += sudoku[j][i]
        if row != 45 or col != 45:
            flag = True
    if flag:
        print('#{} 0'.format(tc))
    else:
        print('#{} 1'.format(tc))


# flag, set 사용
# 사각형 확인 함수
def chk_square(sdoku, c):
    number = set()
    for i in range(3):
        for j in range(3):
            number.add(sdoku[i][j+c])
    # 사각형 안의 수의 갯수가 9가 아니라면, 반복이 있는 것이므로 flag=True
    if len(number) != 9:
        return True
    return False
 
T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    flag = False
    for i in range(9):
        # flag=True이면 반복문 탈출
        if flag:
            break
        # 행과 열의 숫자를 담아둘 set() 생성
        row, col = set(), set()
        for j in range(9):
            # 3*3사각형은 index가 0, 3, 6일때만 검사하면 된다.
            if i % 3 == 0 and j % 3 ==0:
                flag = chk_square(sudoku[i:i+3], j)
            row.add(sudoku[i][j])
            col.add(sudoku[j][i])
        # 행 또는 열의 수의 갯수가 9가 아니라면, 반복이 있는 것이므로 flag=True
        if len(row) != 9 or len(col) != 9:
            flag = True
    if flag:
        print('#{} 0'.format(tc))
    else:
        print('#{} 1'.format(tc))
