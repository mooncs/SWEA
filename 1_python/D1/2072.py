'''
2072. 홀수만 더하기

10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.

[입력]
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1 

[출력]
#1 200
#2 208
#3 121
'''
times = int(input())
for time in range(1, times+1):
    num_lst = list( map(int, input().split()) )
    total = 0
    for num in num_lst:
        if num % 2:
            total += num
    print(f'#{time} {total}')