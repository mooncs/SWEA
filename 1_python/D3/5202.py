# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크
from collections import deque
for tc in range(1, int(input())+1):
    n = int(input())
    schedules = deque(sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:x[1]))

    cnt = 1
    end_time = schedules.popleft()[1]
    while schedules:
        s, e = schedules.popleft()
        if s >= end_time:
            end_time = e
            cnt += 1
    print('#{} {}'.format(tc, cnt))


# for tc in range(1, int(input())+1):
#     n = int(input())
#     schedules = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:x[1])

#     cnt = 1
#     end_time = schedules.pop(0)[1]
#     while schedules:
#         s, e = schedules.pop(0)
#         if s >= end_time:
#             end_time = e
#             cnt += 1
#     print('#{} {}'.format(tc, cnt))