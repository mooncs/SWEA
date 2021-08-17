# 3143. 가장 빠른 문자열 타이핑
T = int(input())
for tc in range(1, T+1):
    A, B = input().split()      #문자열 A, B
    la, lb = len(A), len(B)     #문자열 A, B의 길이

    cnt = 0 # 문자열 B가 A에 들어있는 횟수 count
    i = 0   # index
    while i <= la-lb:
        # B와 A의 slicing이 같으면, 카운트하고 index는 B의 길이 후부터 다시 탐색
        if A[i:i+lb] == B:
            cnt += 1
            i += lb
        # 같지 않다면, 다음 index부터 탐색
        else:
            i += 1
    # 키를 누를 횟수 계산        
    press = la - (cnt*lb) + cnt

    print('#{} {}'.format(tc, press))