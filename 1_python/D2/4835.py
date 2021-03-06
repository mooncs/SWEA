'''
4835. 구간합

N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
v 1 2 3 4 5

v '1 2 3' 4 5
이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
 
v 1 2 '3 4 5'
이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
 
답은 12와 6의 차인 6을 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[입력 예시]
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176	 

[출력 예시]
#1 21
#2 11088
#3 1090
'''
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     numbers = list(map(int, input().split()))
#     # M개의 합이 가장 큰 경우와 가장 작은 경우를 담을 변수 min_sum, max_sum정의
#     min_sum = 1000000
#     max_sum = 0
#     for i in range(N-M+1):
#         # M개의 합을 sum에 담고
#         sum = 0
#         for j in range(M):
#             sum += numbers[i+j]
#         # max_sum보다 크다면 max_sum 갱신
#         if sum > max_sum:
#             max_sum = sum
#         # max_sum보다 작다면 max_sum 갱신
#         if sum < min_sum:
#             min_sum = sum
    
#     print('#{} {}'.format(tc, max_sum-min_sum))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    base = 0
    for i in range(M):
        base += numbers[i]
    min_sum = max_sum = base

    for i in range(M, N):
        base = base + numbers[i] - numbers[i-M]

        if base < min_sum:
            min_sum = base
        if base > max_sum:
            max_sum = base


    print('#{} {}'.format(tc, max_sum-min_sum))

