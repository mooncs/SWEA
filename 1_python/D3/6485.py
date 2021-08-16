# 6485. 삼성시의 버스 노선
T = int(input())
for tc in range(1, T+1):
    # 1번~5000번의 버스정류장
    # key는 정류장번호, value는 버스가 지나간 횟수
    bus_stop = {i:0 for i in range(1, 5001)}
    # N :버스 노선의 개수
    N =int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        # 버스가 지나는 정류장 카운트 증가
        for i in range(a, b+1):
            bus_stop[i] += 1
    # P개의 버스 정류장에 대해
    P =int(input())
    answer = ''
    for _ in range(P):
        # answer문자열에 입력된 정류장의 버스가 지나간 횟수를 문자열+공백으로 추가
        answer += str(bus_stop.get(int(input())))+' '

    print('#{} {}'.format(tc, answer[:-1]))


# List
T = int(input())
for tc in range(1, T+1):
    # 1번~5000번의 버스정류장
    bus_stop = [0 for i in range(5000)]
    # N :버스 노선의 개수
    N =int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        # 버스가 지나는 정류장 카운트 증가
        for i in range(a-1, b):
            bus_stop[i] += 1
    # P개의 버스 정류장에 대해
    P =int(input())
    answer = ''
    for _ in range(P):
        # answer문자열에 입력된 정류장의 버스가 지나간 횟수를 문자열+공백으로 추가
        answer += str(bus_stop[int(input())-1])+' '

    print('#{} {}'.format(tc, answer[:-1]))