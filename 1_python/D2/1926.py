'''
1926. 간단한 369게임

3 6 9 게임을 프로그램으로 제작중이다. 게임 규칙은 다음과 같다.
1. 숫자 1부터 순서대로 차례대로 말하되, “3” “6” “9” 가 들어가 있는 수는 말하지 않는다.
  1 2 3 4 5 6 7 8 9…
2. "3" "6" "9"가 들어가 있는 수를 말하지 않는대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다.  
예를 들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야 한다.

입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를 게임 규칙에 맞게 출력하는 프로그램을 작성하라.
박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.
여기서 주의해야 할 것은 박수 한 번 칠 때는 - 이며, 박수를 두 번 칠 때는 - - 가 아닌 -- 이다. 
 
[제약사항]
N은 10이상 1,000이하의 정수이다. (10 ≤ N ≤ 1,000)

[입력]
10

[출력]
1 2 - 4 5 - 7 8 - 10
'''
from itertools import count


N = int(input())
result = ''

for i in range(1, N+1):
    cnt = 0
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        cnt += str(i).count('3') + str(i).count('6') + str(i).count('9')
        result += ('-'*cnt+' ')

    else:
        result += (str(i) + ' ')

print(result[:-1])


# # 2
# N = int(input())                        # 몇 번 돌아갈지 입력받기
# arr = [str(i) for i in range (1, N+1)]  # 1~N까지 숫자를 리스트에 담기
# lst = ['3', '6', '9']                   # 체크해야할 3, 6, 9 리스트에 담기
# answer = []
# for num in arr:
#   cnt = 0                               # 3, 6, 9가 몇 개 들어가는지 개수 세기
#   for n in num:                         # 두 자리 이상일 경우 하나 하나 판단
#     if n in lst:
#       cnt += 1
#   if cnt != 0:                          # 3, 6, 9가 1개 이상 들어가면, 들어간만큼 숫자를 추가
#     answer.append(cnt)
#   else:                                 # 아닐경우 원래 숫자 추가
#     answer.append(num)

# for i in answer:
#   if type(i) == str:                    # 문자열인 경우 원래 숫자기 때문에 그대로 출력
#     print(i, end=' ')
#   else:                                 # 숫자일 경우 3, 6, 9가 포함된 것이기 때문에 포함된 수 만큼 -출력
#     print('-'*i, end=' ')


# # 3
# N = int(input())
# answer = []
# for i in range(1, N+1):
#   num = str(i)
#   if '3' in num or '6' in num or '9' in num:
#     answer.append( '-' * (num.count('3') + num.count('6') + num.count('9')) )
#   else:
#     answer.append(i)

# for a in answer:
#   print(a, sep=' ')