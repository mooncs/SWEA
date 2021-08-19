# 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기
T = int(input())
for tc in range(1, T+1):
    # 비교할 문자열 입력 받기
    words = list(input())
    # 검색할 현재 위치
    pos = 0
    # 문자열의 길이가 1이 될 때까지 반복
    while len(words) > 1:
        # 현재 탐색 위치가 문자열의 제일 마지막이라면 반복문 탈출
        if pos >= len(words)-1:
            break
        # 현재 탐색 위치의 문자와 다음 위치의 문자가 같다면
        if words[pos] == words[pos+1]:
            # 현위치의 문자를 제거
            words.pop(pos)
            # 다음 위치의 문자 제거
            words.pop(pos)
            # 현 위치가 제일 처음이 아니라면 그 전 위치에서 다시 비교 시작
            if pos > 0:
                pos -= 1
        # 다음 위치의 문자와 같지 않다면 다음 위치 탐색
        else:
            pos += 1
    print('#{} {}'.format(tc, len(words)))



# # 10개의 테스트케이스 중 9개 정답
# T = int(input())
# for tc in range(1, T+1):
#     words = list(input())
#     length = len(words)
#     pos = 0
#     while length > 1 or pos < length-1:
#         if pos >= length-1:
#             break

#         if words[pos] == words[pos+1]:
#             words.pop(pos)
#             words.pop(pos)
#             length = len(words)]
#             pos -= 1
#         else:
#             pos += 1
#     print('#{} {}'.format(tc, length))

