# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2
def bfloat(x):
    cnt, std = 1, 0
    binary = ''
    while cnt < 13:
        if x >= std+2**-cnt:
            std += 2**-cnt
            binary += '1'
        else:
            binary += '0'
        if x == std:
            return binary
        cnt += 1
    return 'overflow'

for tc in range(1, int(input())+1):
    num = float(input())
    print('#{} {}'.format(tc, bfloat(num)))
