import sys
sys.stdin = open("c:/Users/csmoo/OneDrive/바탕 화면/python/SWEA/1_python/D5/input.txt", "r")

num = {'0001101':'0', '0011001':'1', '0010011':'2', '0111101':'3', '0100011':'4', 
'0110001':'5','0101111':'6', '0111011':'7', '0110111':'8', '0001011':'9'}
            
def decode(arr, size):
    arr = arr[::size]
    result = ''
    for i in range(8):
        pwd = num.get(arr[i*7:(i*7)+7], -1)
        if pwd == -1:return 0
        result += pwd
    return result

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    codes, pwds = set(), set()
    for _ in range(n):
        hnum = input().strip().rstrip('0')
        if hnum:codes.add(hnum)

    for code in codes:
        bnum = bin(int(code,16))[2:].rstrip('0')
        size = 1
        max_size = len(bnum)//56 + 1
        while bnum and size <= max_size:
            bnum = bnum.zfill(size*56)
            temp = bnum[-(size)*56:]
            result = decode(temp, size)
            if result:
                pwds.add(result)
                bnum = bnum[:-size*56].rstrip('0')
                size = 1
            else:
                size += 1
    for pwd in pwds:
        answer, chk = 0, 0
        for i in range(0, 8, 2):
            chk += int(pwd[i])*3
            chk += int(pwd[i+1])
        if chk%10:continue
        else:answer += sum(list(map(int, pwd)))
    print("#{} {}".format(tc, answer))