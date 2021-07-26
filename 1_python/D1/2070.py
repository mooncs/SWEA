'''
2070. 큰 놈, 작은 놈, 같은 놈

2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.


[입력]
3
3 8 
7 7 
369 123      

[출력]
#1 <
#2 =
#3 >
'''
times = int(input())
for time in range(1, times+1):
    x, y = map(int, input().split())
    if x > y:
        print(f'#{time} >')
    elif x < y:
        print(f'#{time} <')
    else:
        print(f'#{time} =')