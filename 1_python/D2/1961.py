'''
1961. 숫자 배열 회전

N x N 행렬이 주어질 때,
시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

[제약 사항]
N은 3 이상 7 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N이 주어지고,
다음 N 줄에는 N x N 행렬이 주어진다.

[출력]
출력의 첫 줄은 '#t'로 시작하고,
다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

[입력 예시]
10
3
1 2 3
4 5 6
7 8 9
6
6 9 4 7 0 5
8 9 9 2 6 5
6 8 5 4 9 8
2 2 7 7 8 4
7 5 1 9 7 9
8 9 3 9 7 6

[출력 예시]
#1
741 987 369
852 654 258
963 321 147
#2
872686 679398 558496
952899 979157 069877
317594 487722 724799
997427 894586 495713
778960 562998 998259
694855 507496 686278
'''
# # 1
# import copy
# T = int(input())
# # 테스트 케이스만큼 수행
# for tc in range(1, T+1):
#     # NxN 행렬의 N 입력
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     # 회전한 것을 담을 행렬
#     turned = copy.deepcopy(matrix)
#     # 최종 결과를 담을 행렬
#     results = copy.deepcopy(matrix)
#     # 90도, 180도, 270도 3번 회전
#     for circle in range(3):
#         # 회전한 값 turned에 갱신
#         for x in range(N):
#             for y in range(N):
#                 turned[x][y] = matrix[N-1-y][x]
        
#         # 회전한 행렬의 한 행의 하나의 문자열로
#         for i in range(len(turned)):
#             a = ''
#             for t in turned[i]:
#                 a += str(t)
#             # 만든 문자열을 결과 행렬에 넣고
#             results[i][circle] = a
#         # 다음 회전할 행렬을, 이전 회전한 행렬로 갱신
#         matrix = copy.deepcopy(turned)
#     # 테스트 케이스 번호를 출력하고
#     print('#{}'.format(tc))
#     for result in results:
#         # 3회전의 결과밖에 없음으로 열은 3까지만 필요
#         for r in range(3):
#             print(result[r], end=' ')
#         print()

# # 2 아직 이해 불가...
# T = int(input())
 
# for tc in range(T):
#     res = list()
#     arr = [list(input().split()) for _ in range(int(input()))]
#     res.append([''.join(reversed(i)) for i in zip(*arr)])
#     res.append([''.join(reversed(i)) for i in reversed(arr)])
#     res.append([''.join(i) for i in reversed(list(zip(*arr)))])
#     res = list(zip(*res))
#     print(f'#{tc+1}')
#     for i in res:
#         for j in i:
#             print(j, end = ' ')
#         print()

# 3
# 회전 함수 선언
def rotate(origin):
    N = len(origin)
    rotated = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            rotated[x][y] = origin[N-1-y][x]
    return rotated

# 테스트 케이스 입력
T = int(input())
# 테스트 케이스 만큼 수행
for tc in range(1, T+1):
    # NxN 행렬의 N 입력
    N = int(input())
    # 처음 행렬을 담을 변수 선언
    basic = []
    for _ in range(N):
        basic.append(list(map(int,input().split(" "))))

    # 90도 회전 
    r2=rotate(basic)
    # 180도 회전
    r3=rotate(r2)
    # 270도 회전
    r4=rotate(r3)

    # 출력 시작
    print('#{}'.format(tc))
    for i in range(N):
        # unpacking 활용
        print(*r2[i], sep = '', end=' ')
        print(*r3[i], sep = '', end=' ')
        print(*r4[i], sep = '', end=' ')
        print()