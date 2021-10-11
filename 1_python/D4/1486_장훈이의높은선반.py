# 1486. 장훈이의 높은 선반
# # 부분집합
# # 오답 : 10개의 테스트케이스 중 9개가 맞았습니다. =>  tower>b→tower>=b
# for tc in range(1, int(input())+1):
#     n, b = map(int, input().split())
#     height = list(map(int, input().split()))
#     diff = 200000
#     # 1<<n 부분집합의 개수
#     for i in range(1<<n):
#         tower = 0
#         for j in range(n):
#             # i의 j번째 비트가 1이면
#             if i & 1<<j:
#                 tower += height[j]
#             if tower>=b and diff<tower-b:break
#         else:
#             if tower>=b:diff=tower-b

#     print('#{} {}'.format(tc, diff))


# 재귀
def recursion(i, tower):
    global diff
    if i == n:                          # 끝 순서까지 다 돌았을 경우
        if tower >= b and tower-b<diff: # 선반의 높이보다 높고 그 차이가 최소일 경우
            diff=tower-b
        return
    if tower >= b and tower-b>diff:return
    recursion(i+1, tower)               # 해당 순서의 점원을 포함하지 않을 경우
    recursion(i+1, tower+height[i])     # 해당 순서의 점원의 키를 포함했을 경우

for tc in range(1, int(input())+1):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    diff = 200000
    recursion(0, 0)
    print('#{} {}'.format(tc, diff))
