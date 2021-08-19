# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
for tc in range(1, 11):
    # 문자열의 길이 N, 0~9로 이루어진 번호 문자열 nums
    N, nums = input().split()
    # 번호 문자열을 검사할 리스트
    st = []
    for i in range(int(N)):
        # 검사 리스트가 비어있다면, 현재의 번호 문자열 추가
        if not st:
            st.append(nums[i])
        else:
            # 현재의 번호 문자열이 이전 번호 문자열과 동일하다면
            if nums[i]==st[-1]:
                # 이전의 번호 문자열 제거
                st.pop()
            # 현재의 번호 문자열이 이전 번호 문자열과 다르다면
            else:
                # 검사 리스트에 추가
                st.append(nums[i])
    # 최종 password를 담을 문자열
    password = ''
    # 연속되지 않은 번호 문자열을 담은 리스트에서 문자열 하나씩을 더해서 password 완성
    for s in st:
        password += s

    print('#{} {}'.format(tc, password))