# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기
T = int(input())
for tc in range(1, T+1):
    # 20 X N, 직사각형 채우기
    # 조건 An = An-1 + 2An-2
    N = int(input())
    # N은 10의 배수이기 때문에 A1, A2, ...와 같은 형식으로 만들기 위해 N을 10으로 나누기
    N //= 10
    # A0은 사용하지 않기 때문에, A1~An까지 N+1개 생성
    matrix = [0]*(N+1)
    # A1, A2는 수식 활용 불가하기 때문에 먼저 정의
    matrix[1] = 1
    matrix[2] = 3
    # A3부터는 수식에 대입
    if N > 2:
        for i in range(3, N+1):
            matrix[i] = matrix[i-1] + 2*matrix[i-2]
    
    print('#{} {}'.format(tc, matrix[N]))
    



