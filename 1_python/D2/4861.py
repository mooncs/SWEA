# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = ''
    for i in range(N):
        # 가로로 회문 탐색
        for j in range(N-M+1):
            for k in range(M//2):
                # 회문이 아니라면 반복문 탈출
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
            # break 없이 반복문을 다 돌았으면 회문이므로, 정답에 추가
            else:
                for a in arr[i][j:j+M]:
                    ans += a
                break
        # 가로 검색에서 회문이 안나왔다면, 세로 검색에 회문 존재
        else:
            for j in range(N-M+1):
                for k in range(M//2):
                    if arr[j+k][i] != arr[j+M-1-k][i]:
                        break
                # break 없이 반복문을 다 돌았으면 회문이므로, 정답에 추가    
                else:
                    for l in range(j, j+M):
                        ans += arr[l][i]
                    break

    print('#{} {}'.format(tc, ans))


