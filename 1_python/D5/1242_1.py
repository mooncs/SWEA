# 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔
# # Runtime Error!
# num = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5,'0101111':6, '0111011':7, '0110111':8, '0001011':9}

# def dtob(codes):
#     bnum = ''
#     binary = []
#     for code in codes:
#         bnum += '{:04d}'.format(int(bin(int(code,16))[2:]))
#     while len(bnum)>55:
#         for i in range(len(bnum)-1, -1, -1):
#             if bnum[i] == '1':
#                 binary.append(bnum[i-55:i+1])
#                 bnum = bnum[0:i-55]
#                 break
#     return binary

# for tc in range(1, int(input())+1):
#     n, m = map(int, input().split())
#     codes = []
#     for _ in range(n):
#         code = input().strip('0')
#         if code and code not in codes:
#             codes.append(code)
#     pwds = []
#     for code in codes:
#         for b in dtob(code):
#             if b not in pwds:
#                 pwds.append(b)
#     for pwd in pwds:
#         result = [num.get(pwd[7*i:7*i+7]) for i in range(8)]
#         chk = (result[0] + result[2] + result[4] + result[6]) * 3 + (result[1]+result[3]+result[5]) + result[7]
#         # chk가 10의 배수라면, 암호코드 숫자들의 합 출력
#         if chk%10 == 0:
#             print('#{} {}'.format(tc, sum(result)))
#             break

# import sys
# num = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5,'0101111':6, '0111011':7, '0110111':8, '0001011':9}
# def dtob(codes):
#     bnum = ''
#     binary = []
#     for code in codes:
#         bnum += '{:04d}'.format(int(bin(int(code,16))[2:]))
#     while len(bnum)>55:
#         bnum = bnum.rstrip('0')
#         if len(bnum) < 56:
#             bnum = '{:056d}'.format(int(bnum))
#         binary.append(bnum[len(bnum)-56:len(bnum)])
#         bnum = bnum[:len(bnum)-56]
#     return binary

# for tc in range(1, int(input())+1):
#     n, m = map(int, input().split())
#     codes = []
#     for _ in range(n):
#         # code = input().strip('0')
#         code = sys.stdin.readline().rstrip().strip('0')
#         if code and code not in codes:
#             codes.append(code)
#     pwds = []
#     for code in codes:
#         for b in dtob(code):
#             if b not in pwds:
#                 pwds.append(b)
#     answer = 0
#     for pwd in pwds:
#         result = [num.get(pwd[7*i:7*i+7]) for i in range(8)]
#         chk = (result[0] + result[2] + result[4] + result[6]) * 3 + (result[1]+result[3]+result[5]) + result[7]
#         # chk가 10의 배수라면, 암호코드 숫자들의 합 출력
#         if chk%10 == 0:
#             answer += sum(result)
#     print('#{} {}'.format(tc, answer))

# (오답 : 20개의 테스트케이스 중 12개가 맞았습니다.)
import sys
sys.stdin = open("c:/Users/csmoo/OneDrive/바탕 화면/python/SWEA/1_python/D5/input.txt", "r")
decode = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5,'0101111':6, '0111011':7, '0110111':8, '0001011':9}

def test(arr):
    result = 0
    for i in range(0, 8, 2):
        result += arr[i]*3
        result += arr[i+1]
    if result%10:return 0
    else:return sum(arr)

def chk(arr, size):
    temp = arr[-(size)*56:]
    complete = []
    for i in range(0, len(temp), size*7):
        pwd = decode.get(temp[i:i+(size*7)][::size], -1)
        if pwd == -1:return 0
        complete.append(pwd)
    return tuple(complete)

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    codes, pwds = set(), set()
    for _ in range(n):
        hnum = input().strip().rstrip('0')
        if hnum:codes.add(hnum)

    for code in codes:
        bnum = bin(int(code,16))[2:].rstrip('0')
        while bnum:
            size = 1
            while True:
                # zfill : 문자열 또는 숫자 앞에 0을 채우기
                bnum = bnum.zfill(size*56)
                result = chk(bnum, size)
                if result:
                    pwds.add(result)
                    bnum = bnum[:len(bnum)-size*56].rstrip('0')
                    break
                size += 1
    print("#{} {}".format(tc, sum(test(p) for p in pwds)))