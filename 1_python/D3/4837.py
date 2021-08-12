# 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
def my_sum(number):
    total = 0
    for n in number:
        total += n
    return total

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [i for i in range(1, 13)]
    cnt =0
    for i in range(1<<len(A)):      # 부분 집합의 개수 0~2n-1 각각의 부분집합
        subset = []
        for j in range(len(A)):     # 어떤 원소를 가진 부분집합인지 확인하기 위해서 반복문 실행
            if i & (1<<j):          # 1을 한 칸씩 이동하며, 어떤 원소를 부분집합에 넣을지 판단
                subset.append(A[j])
        if len(subset) == N and my_sum(subset) == K:
            cnt += 1
    
    print('#{} {}'.format(tc, cnt))