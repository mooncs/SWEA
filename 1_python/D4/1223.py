# 1223. [S/W 문제해결 기본] 6일차 - 계산기2
for tc in range(1, 11):
    operator = {'+':2, '*':1}
    n = int(input())        # 문자열 계산식의 길이, n 
    t_cal = list(input())   # 문자열 계산식, t_cal
    stack = []              # stack
    postfix = ''            # 후위 표기식, psotfix
    # 후위 표기식 변경
    for t in t_cal:
        if t == '+' or t == '*':
            # 스택에 이미 연산자가 있고, 스택의 top의 우선순위와 비교해서 우선순위가 더 낮다면 연산자 pop 후위 표기식에 추가
            if stack and operator.get(stack[-1]) < operator.get(t):
                while stack:
                    postfix += stack.pop()
            # 연산자 스택에 push
            stack.append(t)
        # 숫자면 그냥 후위 표기식에 추가
        else:
            postfix += t
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
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1+num2)

    print('#{} {}'.format(tc, stack[0]))