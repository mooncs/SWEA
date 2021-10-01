# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수
for tc in range(1, int(input())+1):
    # 자리수 n, 16진수 hnum
    n, hnum = input().split()
    # 16진수를 10진수로, 10진수를 2진수로 변환
    bnum = bin(int(hnum, 16))[2:]
    # 앞자리가 0인 경우 0이 출력이 안되기 때문에
    # 길이를 비교해서 작으면 앞에 0을 붙이고
    if len(bnum) < int(n)*4:print('#{} {}'.format(tc, '0'+bnum))
    # 그렇지 않으면 그냥 출력
    else:print('#{} {}'.format(tc, bnum))

# # Runtime Error!
# def htod(x):
#     if '0' <= x <= '9':return int(x)
#     else:return ord(x)-55

# def dtob(x):
#     binary = ''
#     while x > 0:
#         x, r = divmod(x, 2)
#         binary = str(r) + binary
#     return '{:04d}'.format(int(binary))

# for tc in range(1, int(input())+1):
#     n, hnum = input().split()
#     dnum = [htod(h) for h in hnum]
#     bnum = ''
#     for d in dnum:
#         bnum += dtob(d)
    
#     print('#{} {}'.format(tc, bnum))