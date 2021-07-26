'''
2029. 몫과 나머지 출력하기

2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

[제약 사항]
각 수는 1이상 10000이하의 정수이다.


[입력]
3   
9 2  
15 6 
369 15  

[출력]
#1 4 1
#2 2 3
#3 24 9
'''
times = int(input())

for time in range(1, times+1):
    x, y = map(int, input().split())
    print(f'#{time} {x//y} {x%y}')
