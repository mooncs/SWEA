# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교
T = int(input())
for tc in range(1, T+1):
    str1 = input()              # 첫 번째 문자열 입력
    str2 = input()              # 두 번째 문자열 입력
    N, M = len(str1), len(str2) # 각 문자열의 길이
    for i in range(M-N+1):
        # str2의 slicing 값과 str1이 같으면, 1출력 후 반복문 탈출
        if str2[i:i+N] == str1:
            print('#{} 1'.format(tc))
            break
    # 반복문이 정상적으로 돌았다면, str1과 같은 문자열이 str2에 없는 것이므로 0출력
    else:
        print('#{} 0'.format(tc))
