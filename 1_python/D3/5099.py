# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기
def makePizza(i):
    oven = cheese[:i]                       # 오븐에 들어갈 피자
    pizza = cheese[i:]                      # 남아있는 피자
    while len(oven)>1:                      # 오븐에 하나가 남을때까지
        p = oven.pop(0)                     # 오븐 처음에 있는 피자를 꺼내서
        if p[1]//2:                         # 치즈가 남아있다면,
            oven.append([p[0],p[1]//2])     # 치즈를 반으로 만들고 다시 오븐으로
        else:                               # 치즈가 남아있지 않다면,
            if pizza:                       # 남아있는 피자가 있는지 확인하고
                oven.append(pizza.pop(0))   # 남아있는 피자를 오븐에 넣어준다.
    return oven[0][0]                       # 오븐에 마지막으로 남아있는 피자의 index를 반환
            
T = int(input())
for tc in range(1, T+1):
    # 화덕의 크기 N과 피자 개수 M
    N, M = map(int, input().split())
    # 피자에 뿌려진 치즈의 양
    cheese = list(map(int, input().split()))
    for idx, ch in enumerate(cheese):
        cheese[idx] = [idx, ch]

    print('#{} {}'.format(tc, makePizza(N)+1))