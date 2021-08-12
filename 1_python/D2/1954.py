'''
★★★★
1954. 달팽이 숫자 

달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

[예제]
N이 3일 경우,
1 2 3
8 9 4
7 6 5

N이 4일 경우,
 1  2  3  4
12 13 14  5
11 16 15  6
10  9  8  7

[제약사항]
달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.

[출력]
각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

[입력 예시]
2    
3   
4         
 
[출력 예시]
#1
1 2 3
8 9 4
7 6 5
#2
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
'''
T = int(input())
for tc in range(1, T+1):
    snail = int(input())
    snail_num = [[0]*snail for _ in range(snail)]
    # 방향, 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 입력할 수
    cnt = 1
    # 현 위치
    r, c = 0, -1
    # 방향지시
    d = 0   
    while cnt <= snail**2:
        # 현 위치에서 방향에 맞게 이동한 위치
        mr, mc = r+dr[d], c+dc[d]
        if 0<=mr<snail and 0<=mc<snail and snail_num[mr][mc]==0:
            snail_num[mr][mc] = cnt
            cnt += 1
            # 현 위치 갱신
            r, c = mr, mc
        else:
            # 범위를 넘어가거나, 이미 수가 입력되어 있으면 방향 변경
            d = (d+1)%4

    print(f'#{tc}')
    for num in snail_num:
        print(" ".join(map(str, num)), end='\n')




# T = int(input())
# for tc in range(T):
#     snail = int(input())
#     snail_num = [[0]*snail for i in range(snail)]
    
#     row = 0
#     col = 0
#     direction = "down"

#     for i in range(snail):
#         snail_num[row][col] = i+1
#         col += 1
#     number = snail
#     col -= 1
#     # print(snail_num)
#     move = snail-1

#     while 0 < move:
        
#         if direction=="down":
#             for i in range(move):
#                 row += 1
#                 snail_num[row][col] = number+1
#                 number += 1
#             direction="left"
#             # print(snail_num)
        
#         elif direction=="left":
#             for i in range(move):
#                 col -= 1
#                 snail_num[row][col] = number+1
#                 number += 1
#             direction="up"
#             move -= 1
#             # print(snail_num)
        
#         elif direction=="up":
#             for i in range(move):
#                 row -= 1
#                 snail_num[row][col] = number+1
#                 number += 1
#             direction="right"
#             # print(snail_num)

#         else:
#             for i in range(move):
#                 col += 1
#                 snail_num[row][col] = number+1
#                 number += 1
#             direction="down"
#             move -= 1
#             # print(snail_num)

#     print(f'#{tc+1}')
#     for num in snail_num:
#         print(" ".join(map(str, num)), end='\n')