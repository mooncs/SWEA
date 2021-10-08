# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬
def partition(arr, s, e):
    pivot = arr[s]
    i, j = s+1, e
    while i <= j:
        while i <= j and arr[i]<=pivot:
            i += 1
        while i <= j and arr[j]>=pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[s], arr[j] = arr[j], arr[s]
    return j

def quickSort(arr, s, e):
    if s < e:
        standard = partition(arr, s, e)
        quickSort(arr, s, standard-1)
        quickSort(arr, standard+1, e)

for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr, 0, n-1)
    print('#{} {}'.format(tc, arr[n//2]))