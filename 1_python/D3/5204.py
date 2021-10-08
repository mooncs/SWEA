# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬
def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    li, ri = 0, 0
    l, r = len(left), len(right)
    result = []
    while li < l or ri < r:
        if li < l and ri < r:
            if left[li] <= right[ri]:
                result.append(left[li])
                li += 1
            else:
                result.append(right[ri])
                ri += 1
        elif li < l:
            result += left[li:]
            break
        elif ri < r:
            result += right[ri:]
            break
    return result

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    print('#{} {} {}'.format(tc, mergeSort(arr)[n//2], cnt))

# # 제한시간 초과
# def merge(left, right):
#     global cnt
#     if left[-1] > right[-1]:
#         cnt += 1
#     result = []
#     while len(left) or len(right):
#         if len(left) and len(right):
#             if left[0] <= right[0]:
#                 result.append(left.pop(0))
#             else:
#                 result.append(right.pop(0))
#         elif len(left):
#             result += left
#             left = []
#         elif len(right):
#             result += right
#             right = []
#     return result

# def mergeSort(arr):
#     if len(arr) == 1:
#         return arr
#     mid = len(arr)//2
#     left = mergeSort(arr[:mid])
#     right = mergeSort(arr[mid:])
#     return merge(left, right)

# for tc in range(1, int(input())+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#     print('#{} {} {}'.format(tc, mergeSort(arr)[n//2], cnt))

# # 병합 정렬 구현
# def merge(left, right):
#     result = []
#     while len(left) or len(right):
#         if len(left) and len(right):
#             if left[0] <= right[0]:
#                 result.append(left.pop(0))
#             else:
#                 result.append(right.pop(0))
#         elif len(left):
#             result += left
#             left = []
#         elif len(right):
#             result += right
#             right = []
#     return result

# def mergeSort(arr):
#     if len(arr) == 1:
#         return arr
#     mid = len(arr)//2
#     left, right = arr[:mid], arr[mid:]
#     left = mergeSort(left)
#     right = mergeSort(right)
#     return merge(left, right)

# for tc in range(1, int(input())+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
    
#     print(mergeSort(arr))