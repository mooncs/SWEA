# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반
for tc in range(1, int(input())+1):
    freight, truck = map(int, input().split())
    weights = sorted(list(map(int, input().split())), reverse=True)
    capacity = sorted(list(map(int, input().split())), reverse=True)
    answer = 0
    f, t = 0, 0
    while f<freight and t<truck:
        if weights[f] <= capacity[t]:
            answer += weights[f]
            f += 1 
            t += 1
        else:
            f += 1
    print('#{} {}'.format(tc, answer))