# 1224. [S/W 문제해결 기본] 6일차 - 계산기3
for tc in range(1, 11):
    n = int(input())        # 문자열 계산식의 길이, n 
    t_cal = list(input())   # 문자열 계산식, t_cal
    stack = []              # stack
    postfix = ''            # 후위 표기식, psotfix
    # 연산자 우선순위 설정
    operator = {'(':3, ')':3, '+':2, '-':2, '*':1, '/':1}
    # 후위 표기식으로 변경
    for t in t_cal:
        # 숫자면 그냥 후위 표기식에 추가
        if '0' <= t <= '9':
            postfix += t
        # 연산자일 경우
        else:
            # 여는 괄호의 경우 스택에 push
            if t == '(':
                stack.append(t)
            # 닫는 괄호의 경우, 여는 괄호를 만날 때까지 pop
            elif t == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop() # 여는 괄호 pop
            # 스택에 이미 연산자가 있고, 스택의 top의 우선순위와 비교해서 우선순위가 더 낮다면 연산자 pop 후위 표기식에 추가
            else:
                while stack and operator.get(stack[-1]) < operator.get(t):
                    postfix += stack.pop()
                # 연산자 스택에 push
                stack.append(t)
        
    # stack빌 때까지 연산자 빼주기
    while stack:
        postfix += stack.pop()

    # 계산
    for p in postfix:
        # 숫자면 스택에 push
        if '0' <= p <= '9':
            stack.append(int(p))
        # 연산자면 스택에서 숫자 두개를 순서대로 pop, 더한 후 다시 스택에 push
        elif p == '*':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1*num2)
        elif p == '/':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1/num2)
        elif p == '-':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1-num2)
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1+num2)

    print('#{} {}'.format(tc, stack[0]))