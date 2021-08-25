# 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth
T = int(input())
for tc in range(1, T+1):
    # 후위 표기법
    postfix = input().split()
    stack = []
    for i in range(len(postfix)):
        # 문자열이 숫자형태라면, 스택에 숫자를 push
        if postfix[i].isdigit():
            stack.append(int(postfix[i]))
        # '.'은 스택에서 숫자를 꺼내 출력
        elif postfix[i] == '.':
            # 연산을 끝냈는데, 스택에 숫자가 1개 아니라는 것은 error
            if len(stack) != 1:
                print('#{} error'.format(tc))
            else:
                print('#{} {}'.format(tc, stack[0]))
        
        else:
            # 연산자라면, 해당 연산을 하고 결과값을 스택에 push
            try:
                num2, num1 = stack.pop(), stack.pop()
                if postfix[i] == '+':stack.append(num1+num2)
                elif postfix[i] == '-':stack.append(num1-num2)
                elif postfix[i] == '*':stack.append(num1*num2)
                elif postfix[i] == '/':stack.append(num1//num2)
            # 연산자인데, 오류가 발생한다는 것은 숫자보다 연산자가 많다는 것이므로 error
            except:
                print('#{} error'.format(tc))
                break

#####################################################################################
# # 10개 중 9개 맞음
# T = int(input())
# for tc in range(1, T+1):
#     # 후위 표기법
#     postfix = input().split()
#     stack = []
#     for i in range(len(postfix)):
#         # 문자열이 숫자형태라면, 스택에 숫자를 push
#         if postfix[i].isdigit():
#             stack.append(int(postfix[i]))
#         # '.'은 스택에서 숫자를 꺼내 출력
#         elif postfix[i] == '.':
#             print('#{} {}'.format(tc, stack[0]))
        
#         else:
#             # 연산자라면, 해당 연산을 하고 결과값을 스택에 push
#             try:
#                 num2, num1 = stack.pop(), stack.pop()
#                 if postfix[i] == '+':
#                   stack.append(num1+num2)
#                 elif postfix[i] == '-':
#                     stack.append(num1-num2)
#                 elif postfix[i] == '*':
#                     stack.append(num1*num2)
#                 elif postfix[i] == '/':
#                     stack.append(num1//num2)
#             # 연산자인데, 오류가 발생한다는 것은 남은 숫자의 수보다 연산자의 수가 많다는 것을 의미함으로 연산 불가
#             except:
#                 print('#{} error'.format(tc))
#                 break

