# 1222. [S/W 문제해결 기본] 6일차 - 계산기1
for tc in range(1, 11):
    n = int(input())        # 문자열 계산식의 길이, n 
    t_cal = list(input())   # 문자열 계산식, t_cal
    stack = []              # 후위 표기법 사용 stack
    postfix = ''            # 후위 표기식, psotfix
    cal_stack = []          # 계산 사용 스택
    # 후위 표기식 변경
    for t in t_cal:
        if t == '+':
            # 스택에 이미 연산자가 있으면 연산자 pop 후위 표기식에 추가
            if stack:
                postfix += stack.pop()
            # 연산자 스택에 push
            stack.append(t)
        # 숫자면 그냥 후위 표기식에 추가
        else:
            postfix += t
    # 마지막 남아있는, +연산자 후위 표기식에 추가 
    else:
        postfix += stack.pop()

    # 계산
    for p in postfix:
        # 숫자면 스택에 push
        if '0' <= p <= '9':
            cal_stack.append(int(p))
        # 연산자면 스택에서 숫자 두개를 순서대로 pop, 더한 후 다시 스택에 push
        else:
            num2 = cal_stack.pop()
            num1 = cal_stack.pop()
            cal_stack.append(num1+num2)


    print('#{} {}'.format(tc, cal_stack[0]))
