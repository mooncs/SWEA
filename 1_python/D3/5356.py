# 5356. 의석이의 세로로 말해요
T = int(input())
for tc in range(1, T+1):
    # 단어들을 글자 단위로 리스트에 담는다.
    words = [list(input()) for _ in range(5)]
    # 단어들의 길이를 담을 리스트
    length = []
    # 최대 단어 길이
    max_len = 0
    # 단어들의 길이 및 최대 단어 길이 갱신
    for word in words:
        length.append(len(word))
        if max_len < len(word):
            max_len = len(word)
    # 최종 답을 담을 문자열
    answer = ''
    # 최대 단어 길이만큼 반복
    for i in range(max_len):
        for j in range(5):
            # 해당 열의 단어가 i보다 크다면 답안에 추가, 아니라면 이미 다 추가한 것
            if length[j] > i:
                answer += words[j][i]

    print('#{} {}'.format(tc, answer))
