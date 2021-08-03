'''
1945. 간단한 소인수분해

숫자 N은 아래와 같다.
N=2a x 3b x 5c x 7d x 11e
N이 주어질 때 a, b, c, d, e 를 출력하라.

[제약 사항]
N은 2 이상 10,000,000 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
 

[입력 예시]
10  
6791400
1646400
1425600
8575
185625
6480
1185408
6561
25
330750
 
[출력 예시]
#1 3 2 2 3 1
#2 6 1 2 3 0
#3 6 4 2 0 1
#4 0 0 2 3 0
#5 0 3 4 0 1
#6 4 4 1 0 0
#7 7 3 0 3 0
#8 0 8 0 0 0
#9 0 0 2 0 0
#10 1 3 3 2 0
'''
# 1
T = int(input())
numbers = [2, 3, 5, 7, 11]
for test in range(T):
    N = int(input())
    result = ''
    for number in numbers:   
        cnt = 0
        while N % number == 0:
            cnt += 1
            N //= number    
        result += str(cnt) + ' '
    
    print(f'#{test+1} {result[:-1]}')

# # 2
# T = int(input())
# numbers = [2, 3, 5, 7, 11]
# for test in range(T):
#     N = int(input())
#     result = [0]*len(numbers)
#     for i in range(len(numbers)):
#         cnt = 0
#         while N % numbers[i] == 0:
#             cnt += 1
#             N //= numbers[i]
#         result[i] = cnt
#     print("#{} {}".format(test+1, " ".join(map(str, result))))