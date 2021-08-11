'''
4831. 전기버스

A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
 
[예시] 다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.
정류장      0 1 2 3 4 5 6 7 8 9 10
충전기      - o - o - o - o - o -
충전 횟수   - - - 1 - 2 - 3 - - -

[입력]
첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )

[출력]
#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

[입력 예시]
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

[출력 예시]
#1 3
#2 0
#3 4
'''
# T = int(input())
# for line in range(1, T+1):
#     # K : 최대 이동 가능 수, N : 종점, M : 충전기 설치 정류장 수
#     K, N, M = map(int, input().split())
#     # charging : 충전기 설치 정류장 위치
#     charging = list(map(int, input().split()))
#     charging.append(N)

#     # 충전 횟수
#     charge = 0
#     # 이동 가능 수
#     move = K
#     # 현재 위치
#     loca = 0
#     for m in range(M):
#         # 충전기 설치 정류장 도달시 이동 가능 수
#         move -= charging[m]-loca
#         # 이동 가능 수를 넘어서 이동한 경우
#         if move < 0:
#             charge = 0
#             break
#         # 현 위치 갱신
#         loca = charging[m]

#         # if loca >= N:
#         #     break

#         # 남은 이동 가능 수로 다음 충전기 설치 정류장까지 갈 수 있는지 판단
#         # 갈 수 없다면, 충전 회수 추가, 이동 가능 수 최신화
#         if move < charging[m+1]-loca:
#             charge += 1
#             move = K


#     print('#{} {}'.format(line, charge))


# 2
# 버스의 현 위치를 신경쓰지 않고,
def bus(KNM, M, cnt=0):
    if KNM[1] <= KNM[0]:
        return cnt
    for i in range(KNM[0], 0, -1):
        if i in M:
            KNM[1] -= i
            for j in range(len(M)):
                M[j] -= i
            cnt += 1
            return bus(KNM, M, cnt)
    return 0        # 도중에 퍼지면
 
 
T = int(input())
for tc in range(1, T+1):
    KNM = list(map(int, input().strip().split()))
    M = list(map(int, input().strip().split()))
    print("#{} {}".format(tc, bus(KNM, M)))