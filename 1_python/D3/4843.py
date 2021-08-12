# 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

# 정렬 함수
def quickSort(number):
    if len(number) <= 1:
        return number
    base = number[len(number)//2]
    small, equal, large=[], [], []
    for num in number:
        if num > base:
            large.append(num)
        elif num < base:
            small.append(num)
        else:
            equal.append(num)
    return quickSort(small) + equal + quickSort(large)

def selectionSort(number):
    for i in range(len(number)-1):
        min_idx = i
        for j in range(i+1, len(number)):
            if number[min_idx] > number[j]:
                min_idx = j
        number[i], number[min_idx] = number[min_idx], number[i]
    return number

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    # 숫자 리스트를 우선적으로 정렬한다.
    # number = quickSort(number)
    number = selectionSort(number)
    answer = []
    for i in range(1, 11):
        # 인덱스가 홀수일 때는 뒤에서 부터
        if i%2:
            answer.append(number[N-(i//2+1)])
        # 인덱스가 짝수일 때는 앞에서 부터
        else:
            answer.append(number[i//2-1])
    
    print('#{} {}'.format(tc, ' '.join(map(str, answer))))