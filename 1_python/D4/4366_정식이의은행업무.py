# 4366. 정식이의 은행업무
def bank(binary, tenary):
    # 2진수를 10진수로 변환한 값을 담을 리스트
    bchange = []
    # 첫번째자리가 0인 2진수는 없기 때문에 1번째 자리부터 탐색
    for i in range(1, len(binary)):
        # 원래 자리 값을 저장하고
        b = binary[i]
        # 원래 1이었다면 0으로, 0이었다면 1로 변경
        binary[i] = '0' if b == '1' else '1'
        # 변경한 2진수를 10진수로 변환하여 리스트 추가
        bchange.append(int(''.join(binary),2))
        # 변경한 값 원래 값으로
        binary[i] = b
    # 3진수는 0, 1, 2가 올 수 있다.
    num = ['0', '1', '2']
    # 3진수 처음부터 탐색
    for j in range(len(tenary)):
        for n in num:
            # 원래 자리 값을 저장
            t = tenary[j]
            # 원래 값과 다른 값으로 변경
            if t != n:tenary[j] = n
            # 변경한 3진수를 10진수로 변환
            tchange = int(''.join(tenary),3)
            # 변환된 값이 2진수를 변환한 값과 같다면
            if tchange in bchange:
                # 그 값을 반환
                return tchange
            # 변경한 값 원래 값으로
            tenary[j] = t

for tc in range(1, int(input())+1):
    binary = list(input())  # 2진수
    tenary = list(input())  # 3진수
    print('#{} {}'.format(tc, bank(binary, tenary)))