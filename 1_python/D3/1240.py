# 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
num = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5,'0101111':6, '0111011':7, '0110111':8, '0001011':9}
# 암호코드를 찾는 함수
# # 1
# def code():
#     for r in range(n):
#         for c in range(m-1, -1, -1):
#             if data[r][c] == '1':
#                 return data[r][c-55:c+1]
# 2
def code():
    data.sort(reverse=True)
    for c in range(m-1, -1, -1):
        if data[0][c] == '1':
            return data[0][c-55:c+1]
# # 3
# def code():
#     ndata = sorted(data, reverse=True)
#     for c in range(m-1, -1, -1):
#         if ndata[0][c] == '1':
#             return ndata[0][c-55:c+1]

for tc in range(int(input())):
    n, m = map(int, input().split())
    data = [input() for _ in range(n)]
    pwd = code()
    result = [num.get(pwd[7*i:7*i+7]) for i in range(8)]
    # (홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드
    chk = (result[0] + result[2] + result[4] + result[6]) * 3 + (result[1]+result[3]+result[5]) + result[7]
    # chk가 10의 배수가 아니라면, 0 출력
    if chk % 10:print('#{} {}'.format(tc+1, 0))
    # chk가 10의 배수라면, 암호코드 숫자들의 합 출력
    else:print('#{} {}'.format(tc+1, sum(result)))