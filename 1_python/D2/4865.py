# 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수
T = int(input())
for tc in range(1, T+1):
    str1 = input()              # 첫 번째 문자열 입력
    str2 = input()              # 두 번째 문자열 입력

    chk = {s:0 for s in str1}   # 카운트할 딕셔너리 생성
    for i in str1:
        if chk.get(i) != 0:     # 이미 카운트한 알파벳이라면 넘어가고
            continue
        for j in str2:
            if i == j:          # 두 값이 같으면 카운트
                chk[i] += 1
    # 딕셔너리의 value값만 가져와서 카운트 횟수 비교
    ans = [value for value in chk.values()]
    max_v = ans[0]              # value의 최대값
    for a in ans:
        if max_v < a:
            max_v = a
    print('#{} {}'.format(tc, max_v))
