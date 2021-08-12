'''
1966. 숫자를 정렬하자

주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.

[제약 사항]
N 은 5 이상 50 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
# SelectionSort
for tc in range(int(input())):
    N = int(input())
    numbers = list( map(int, input().split()) )
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    print('#{} {}'.format(tc+1, ' '.join(map(str, numbers))))

    # answer = ''
    # for number in numbers:
    #     answer += str(number)+' '

    # print('#{} {}'.format(tc+1, answer[:-1]))

# for tc in range(int(input())):
#     N = int(input())
#     numbers = list( map(int, input().split()) )
#     for n in range(N, 0, -1):
#         for i in range(n-1):
#             if numbers[i] > numbers[i+1]:
#                 numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#     answer = ''
#     for number in numbers:
#         answer += str(number)+' '
    
#     print('#{} {}'.format(tc+1, answer[:-1]))


# for tc in range(int(input())):
#     N = int(input())
#     numbers = list( map(int, input().split()) )
#     # 0~9까지 갯수를 셀 리스트 생성
#     counts = [0]*51
#     # 각 숫자별 발생 횟수를 저장한다.
#     for number in numbers:
#         counts[number] += 1
#     # 발생 횟수 누적합을 구한다. 
#     for i in range(50):
#         counts[i+1] += counts[i]
#     results = [0]*N
#     for i in range(N-1, -1, -1):
#         results[counts[numbers[i]]-1] = numbers[i]

#     answer = ''
#     for result in results:
#         answer += str(result)+' '


#     print('#{} {}'.format(tc+1, answer[:-1]))

