'''
4828. min max

N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

[입력]
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[입력 예시]
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175	 

[출력 예시]
#1 630739
#2 740510
#3 838110
'''
# 최대값 찾는 함수
def find_max(numbers):
    for n in range(len(numbers)-1):
        if numbers[n] > numbers[n+1]:
            numbers[n], numbers[n+1] = numbers[n+1], numbers[n]
    return numbers[-1]

def find_max2(numbers):
    max_num = numbers[1]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num

# 최소값 찾는 함수
def find_min(numbers):
    for n in range(len(numbers)-1, 0, -1):
        if numbers[n] < numbers[n-1]:
            numbers[n-1], numbers[n] = numbers[n], numbers[n-1]
    return numbers[0]

def find_min2(numbers):
    min_num = numbers[1]
    for number in numbers:
        if number < min_num:
            min_num = number
    return min_num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 최대/최소값을 구하고
    max_num = find_max(numbers)
    min_num = find_min(numbers)
    # 테스트 케이스 번호와 최대, 최소값의 차이를 출력
    print('#{} {}'.format(tc, max_num-min_num))

