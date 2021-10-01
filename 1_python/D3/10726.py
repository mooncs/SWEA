# 10726. 이진수 표현
def switch(x):
    for _ in range(n):
        # 마지막 n까지의 비트 중 하나라도 0이면 OFF
        if x%2 == 0:return 'OFF'
        x //= 2
    # 마지막 N 비트가 모두 1이라면 ON
    return 'ON'

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    print('#{} {}'.format(tc, switch(m)))
