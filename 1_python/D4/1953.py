# 1953. [모의 SW 역량테스트] 탈주범 검거
from collections import deque

T = int(input())
for tc in range(1, T+1):
    # 지하 터널 지도의 세로 크기 N, 가로 크기 M
    # 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C
    # 탈출 후 소요된 시간 L
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    queue = deque()
    # 시작점 enqueue
    queue.append((R, C))