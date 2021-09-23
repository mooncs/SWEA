# 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = [0]
    # 최소heap 만들기
    for num in nums:
        heap.append(num)
        idx = len(heap)-1
        # 부모 노드와 비교해서 부모 노드가 자식 노드보다 크면 swap
        while idx > 1 and heap[idx] < heap[idx//2]:
            heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            # swap했다면 루트 노드까지 계속 비교
            idx //= 2
    # 노드 합 구하기    
    answer = 0
    while N > 0:
        N //= 2
        answer += heap[N]
    print('#{} {}'.format(tc, answer))
        

    