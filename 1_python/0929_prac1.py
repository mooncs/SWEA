# 0과 1로 이루어진 1차 배열에서 7개 byte를 묶어서 10진수로 출력하기
# 0000000111100000011000000111100110000110000111100111100111111001100111
data = list(map(int, input()))          # 데이터 입력 받기
for i in range(0, len(data), 7):        # 7개 단위로 확인
    answer = 0                          # 정답을 계산할 변수
    for j in range(7):                  # 7개를 차례로 계산
        if data[i+j]:                   # 해당 자리수가 1이면
            answer += data[i+j]*2**(6-j)# 10진수로 변환한 수를 더한다.
    print(answer, end=' ')              # 더한값 출력

