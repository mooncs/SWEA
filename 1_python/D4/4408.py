# 4408. 자기 방으로 돌아가기
# ★★★, idea참고
def SelectionSort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]    # 기준이 될 원소

    left = [x for x in arr if x < pivot]    # 기준보다 작으면 왼쪽으로
    equal = [x for x in arr if x == pivot]  # 기준과 동일하다면
    right = [x for x in arr if x > pivot]   # 기준보다 크다면 오른쪽으로

    return QuickSort(left)+equal+QuickSort(right)

T = int(input())
for tc in range(1, T+1):
    # 돌아가야 할 학생들의 수 N
    N = int(input())
    # [현재방, 돌아갈 방]
    moves = [list(map(int, input().split())) for _ in range(N)]
    # 1~400번 복도를 몇 번 지나가는지 카운트 할 리스트
    # 방은 2개씩 마주보므로 총 200칸의 복도 필요, 0번 복도는 없으므로 201개의 복도 생성 
    corridor = [0]*201

    for move in moves:
        # 번호가 작은 방에서 큰 방으로 이동하도록
        if move[0] > move[1]:
            st = (move[1]+1) // 2
            ed = (move[0]+1) // 2
        else:
            st = (move[0]+1) // 2
            ed = (move[1]+1) // 2
        # 지나가는 복도 카운트
        for i in range(st, ed+1):
            corridor[i] += 1
    
    # corridor = SelectionSort(corridor)
    corridor = QuickSort(corridor)
    print('#{} {}'.format(tc, corridor[-1]))
    

###########################################################################
# # 예시o, Runtime error
# def my_sort(arr):
#     if arr[0] > arr[1]:
#         arr[0], arr[1] = arr[0], arr[1]

# T = int(input())
# for tc in range(1, T+1):
#     # 돌아가야 할 학생들의 수 N
#     N = int(input())
#     # [현재방, 돌아갈 방]
#     move = [list(map(int, input().split())) for _ in range(N)]
#     # 번호가 작은 방에서 큰 방으로 돌아가도록
#     for m in move:
#         my_sort(m)

#     st=[]
#     st.append(move[0])
#     cnt = 1
#     for i in range(1, N):
#         for j in range(len(st)):
#             if move[i][0] > st[j][0] and move[i][0] > st[j][1]:
#                 st.append(move[i])
#             else:
#                 cnt += 1
#                 st = []
#                 st.append(move[i])

#     print('#{} {}'.format(tc, cnt))

###########################################################################
# # 예시o, test 2/10 큰 곳에서 작은 곳으로 가는 것을 생각하지 않음
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     move = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 1
#     i, j = 0, 1
#     while i < N-1 and j < N:
#         if move[i][1] < move[j][0] and move[j-1][1] < move[j][0]:
#             j += 1
        
#         else:
#             cnt += 1
#             i += 1

#     print('#{} {}'.format(tc, cnt))

