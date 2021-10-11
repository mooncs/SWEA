# 1970. 쉬운 거스름돈
for tc in range(1, int(input())+1):
    change = int(input())
    money_cnt = {50000:0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0}
    for money, cnt in money_cnt.items():
        cnt += change//money
        change %= money
        money_cnt[money] = cnt
    print('#{}'.format(tc))
    print(*money_cnt.values())