# 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사
# 함수로 만들기
def bracket():
    for d in data:
        # 괄호를 여는 (, { 일 경우 stack에 append
        if d == '(' or d == '{':
            st.append(d)
        # 괄호를 닫는 ), } 일 경우
        elif d == ')' or d == '}':
            # stack에 아무것도 없을 경우, 괄호가 열리지 않은 것이기 때문에 return 0
            if len(st) == 0:
                return 0
            # 그렇지 않을 경우, stack에서 pop
            else:
                chk = st.pop()
            # 괄호의 짝이 맞지 않은 경우, return 0
            if d == ')' and chk == '{':
                return 0
            elif d == '}' and chk == '(':
                return 0
    # 반복문을 다돌았는데도 stack에 무언가 남았다면, 짝이 안 맞는 것이므로 return 0
    if st:
        return 0
    # 모든 것이 문제가 없다면, return 1
    return 1
    
T = int(input())
for tc in range(1, T+1):
    data = input()
    st = []
    print('#{} {}'.format(tc, bracket()))


# T = int(input())
# for tc in range(1, T+1):
#     data = input()
#     st = []
#     for d in data:
#         if d == '(' or d == '{':
#             st.append(d)
#         elif d == ')' :
#             if st:
#                 chk = st.pop()
#                 if chk != '(':
#                     print('#{} 0'.format(tc))
#                     break
#             else:
#                 print('#{} 0'.format(tc))
#                 break
#         elif d == '}':
#             if st:
#                 chk = st.pop()
#                 if chk != '{':
#                     print('#{} 0'.format(tc))
#                     break
#             else:
#                 print('#{} 0'.format(tc))
#                 break
#     else:
#         if st:
#             print('#{} 0'.format(tc))
#         else:
#             print('#{} 1'.format(tc))
        

# 10개중 9개 정답 -> ({)} 1로 출력
# T = int(input())
# for tc in range(1, T+1):
#     data = input()
#     st = []
#     for d in data:
#         if d == '(' or d == '{':
#             st.append(d)
#         elif d == ')' or d == '}':
#             if st:
#                 st.pop()
#             else:
#                 print('#{} 0'.format(tc))
#                 break
#     else:
#         if st:
#             print('#{} 0'.format(tc))
#         else:
#             print('#{} 1'.format(tc))
        
    