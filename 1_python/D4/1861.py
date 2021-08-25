# 1861. 정사각형 방
# 오답 : 27개의 테스트케이스 중 14개가 맞았습니다.
def cntRoom():
    max_cnt = 1
    room = N**2
    drc = [[-1,0],[1,0],[0,-1],[0,1]]       # 상하좌우 이동
    for i in range(N):
        for j in range(N):
            cnt = 1
            q = [(i, j)]
            while q:
                pr, pc = q.pop()    
                for k in range(4):
                    dr, dc = pr+drc[k][0], pc+drc[k][1]
                    if 0<=dr<N and 0<=dc<N and sq[dr][dc]-sq[pr][pc]==1:
                        q.append((dr, dc))
                        cnt += 1
            if cnt>max_cnt:
                max_cnt = cnt
                room = sq[i][j]

            elif cnt == max_cnt :
                if room>sq[i][j]:
                    room = sq[i][j]
    return max_cnt, room


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sq = [list(map(int, input().split())) for _ in range(N)]# N²개의 방
    max_cnt, room = cntRoom()
    print('#{} {} {}'.format(tc, room, max_cnt))
    