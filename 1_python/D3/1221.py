# 1221. [S/W 문제해결 기본] 5일차 - GNS
standard = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for _ in range(int(input())):
    tc, n = input().split()
    numbers = input().split()
    
    answer = []
    for std in standard:
        for num in numbers:
            if std == num:
                answer.append(num)
    print(tc)
    print(' '.join(answer))
