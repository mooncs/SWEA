# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

# 이진탐색 함수생성
def binarySearch(data, key):
    start = 1
    end = data
    cnt = 0
    while start <= end:
        middle = (start+end)//2
        cnt += 1
        if middle == key:
            return cnt
        elif middle < key:
            start = middle
        else:
            end = middle
    return cnt
# 이진탐색 재귀형식 함수생성
def binarySearchRecursion(key, start, end, cnt=1):
    middle = (start+end)//2
    if middle == key:
        return cnt
    elif middle < key:
        return binarySearchRecursion(key, middle, end, cnt+1)
    else:
        return binarySearchRecursion(key, start, middle, cnt+1)

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    # cnt_a = binarySearch(P, A)
    cnt_a = binarySearchRecursion(A, 1, P)
    # cnt_b = binarySearch(P, B)
    cnt_b = binarySearchRecursion(B, 1, P)
    # 이진 탐색의 결과를 비교하여 어떤 것이 계산 과정이 간단한지 출력
    if cnt_a < cnt_b:
        print('#{} A'.format(tc))
    
    elif cnt_a > cnt_b:
        print('#{} B'.format(tc))
    
    else:
        print('#{} 0'.format(tc))