# 2005. 파스칼의 삼각형
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     # 파스칼 삼각형을 담을 이차원 리스트 생성
#     pascal = [[0]*i for i in range(1, N+1)]
#     # 첫 번째 줄은 항상 숫자 1이다.
#     pascal[0][0] = 1
    
#     for j in range(1, N):
#         # 각 행의 처음과 마지막은 항상 1이다.
#         pascal[j][0] = pascal[j][-1] = 1
#         # 그래도 배운 스택을 활용하기 위해...
#         # 이전 행을 스택이 쌓인 상태로 보고, 이전 행의 길이를 top으로, index를 지정할 변수로 k
#         st = pascal[j-1]
#         top = j-1
#         k = 1
#         # top이 이전 행의 제일 처음 숫자를 가리킬 때까지 반복
#         while top:
#             pascal[j][k] = st[top] + st[top-1]
#             top -= 1
#             k += 1

#     print('#{}'.format(tc))
#     # unpacking을 활용한 출력
#     for p in pascal:
#         print(*p)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 파스칼 삼각형을 담을 이차원 리스트 생성
    pascal = [[0]*i for i in range(1, N+1)]
    # 첫 번째 줄은 항상 숫자 1이다.
    pascal[0][0] = 1
    
    for j in range(1, N):
        # 각 행의 처음과 마지막은 항상 1이다.
        pascal[j][0] = pascal[j][-1] = 1
        for k in range(1, j):
            pascal[j][k] = pascal[j-1][k-1] + pascal[j-1][k]

    print('#{}'.format(tc))
    # unpacking을 활용한 출력
    for p in pascal:
        print(*p)