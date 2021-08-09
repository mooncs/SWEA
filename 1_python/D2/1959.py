'''
1959. 두 개의 숫자열

N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.
Ai = 1 5 3
Bj = 3 6 -7 5 4
Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
 
서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.
 
[제약 사항]
N 과 M은 3 이상 20 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
두 번째 줄에는 Ai,
세 번째 줄에는 Bj 가 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

[입력 예시]
10
3 5
1 5 3
...

[출력 예시]
#1 30
#2 63
'''
# # 1
# T = int(input())
# # 입력한 테스트 케이스만큼 실행
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     first = list(map(int, input().split()))
#     second = list(map(int, input().split()))

#     # M이 클 때를 가정하여 코드 작성하였기 때문에, N이 크다면 변수들을 swap
#     if N > M:
#         N, M = M, N
#         first, second = second, first
#     # 횟수를 카운트할 변수 i 설정
#     i = 0
#     # 제일 큰 곱의 합을 담을 변수 multi설정
#     multi = 0
#     # 두 숫자열의 길이의 차만큼 실행
#     while i <= M-N:
#         # 작은 리스트의 길이만큼 긴 리스트의 요소로 이루어진 새로운 리스트 생성
#         new_second = [second[i+idx] for idx in range(N)]
#         # 곱의 합을 담을 변수 hap 설정
#         hap = 0
#         # 두 수의 곱을 hap에 더하고
#         for idx in range(N):
#             hap += first[idx] * new_second[idx]
#         # 최종적인 hap이 multi보다 크다면, 제일 큰 곱의 합 갱신
#         if hap > multi:
#             multi = hap
#         # 횟수 1 증가
#         i += 1

#     print('#{} {}'.format(tc, multi))

# 2
T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    if N > M:
        first, second = second, first
        N, M = M, N
    
    # float('-inf')는 음의 무한대, float('inf')는 양의 무한대
    max_sum = float('-inf')
    for i in range(M-N + 1):
        result = 0
        for j in range(N):
            result += first[j] * second[i + j]
        if result > max_sum:
            max_sum = result
 
    print(f'#{tc} {max_sum}')