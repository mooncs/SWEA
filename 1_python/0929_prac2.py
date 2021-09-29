# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해보자
# 01D06079861D79F99F
data = input()  # 데이터 입력 받기
binary = ''     # 2진수로 데이터를 변화한 값
for d in data:
    # 16진수를 10진수로
    num = ord(d) - 48 if '0' <= d <= '9' else ord(d) - 55
    # 10진수를 2진수로
    # 16진수를 10진수로 변화시켰기 때문에 0~15사이의 수만 존재
    for i in range(3, -1, -1):
        binary += '1' if num & (1<<i) else '0'
# 2진수로 데이터를 변화한 값이 7bit씩 나누어 떨어지지 않는다면
if len(binary)%7:
    q, r = len(binary)//7, len(binary)%7            # 7로 나눈 몫 q, 나머지 r
    for i in range(q):                              # 몫만큼 반복
        answer = 0                                  # 10진수를 계산할 변수
        for j in range(7):                          # 7bit씩 계산
            answer += int(binary[7*i+j])*2**(6-j)   # 10진수로 변환한 수를 더하고
        print(answer, end=' ')                      # 10진수 출력
    answer = 0                                      # 10진수를 계산할 변수
    for j in range(r):                              # 나머지만큼 반복
        answer += int(binary[7*q+j])*2**(r-j-1)     # 10진수로 변환한 수를 더하고
    print(answer)                                   # 10진수 출력
# 2진수로 데이터를 변화한 값이 7bit씩 나누어 떨어진다면
else:
    for i in range(0, len(binary), 7):          # 7개 단위로 확인
        answer = 0                              # 10진수를 계산할 변수
        for j in range(7):                      # 7bit씩 계산
            answer += int(binary[i+j])*2**(6-j) # 10진수로 변환한 수를 더한다.
        print(answer, end=' ')                  # 10진수 출력